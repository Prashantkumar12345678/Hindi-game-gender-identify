# -*- coding: utf-8 -*-
"""Strip the checkerboard off the end-screen GIF and ship it as an animated WebP with real alpha.

The "background" is not a scene, it is the transparency CHECKERBOARD baked in by whatever exported
the file: a 2-4 colour grid of (252,252,255) and (252,252,170) with their darker twins. That makes
it keyable exactly - but a plain colour key would also eat the bird, whose own white IS
(252,252,255), the brightest colour in the frame. So the key is FLOOD-FILLED FROM THE BORDER: only
checker pixels reachable from outside go, and anything the silhouette encloses stays whatever it
is. Same reasoning as the walking-animal GIFs earlier in this project.

Output is WebP, not GIF: GIF alpha is one all-or-nothing index and this art has soft edges, which
under a hard cut show as a ragged fringe on the celebration's sunburst. WebP carries real alpha and
is far smaller for 150+ frames.
"""
import os
from collections import deque
import numpy as np
from PIL import Image, ImageSequence

SRC = "assets/Images/last page gif.gif"
OUT = "assets/Images/last_page_anim.webp"
TARGET_H = 392          # .end-mascot renders ~330px wide; this keeps it crisp
TOL = 26                # how far a pixel may sit from a checker colour and still count as one

im = Image.open(SRC)
frames, durs = [], []
canvas = None
for f in ImageSequence.Iterator(im):
    r = f.convert("RGBA")
    canvas = r.copy() if canvas is None else canvas
    if frames: canvas.alpha_composite(r)
    frames.append(canvas.copy())
    durs.append(f.info.get("duration", 60) or 60)

a0 = np.array(frames[0].convert("RGB")).astype(int)
h, w, _ = a0.shape
# the checker's own colours, taken from the border rather than assumed
border = np.concatenate([a0[0], a0[-1], a0[:, 0], a0[:, -1]])
keys, seen = [], set()
for px in border:
    t = tuple(px)
    if t in seen: continue
    seen.add(t)
    if not any(abs(px - np.array(k)).max() <= TOL for k in keys):
        keys.append(t)
print("checker colours found on the border:", keys)

def alpha_for(rgb):
    """True where the pixel is checker-coloured AND reachable from the frame's edge"""
    d = np.stack([np.abs(rgb - np.array(k)).max(axis=2) for k in keys]).min(axis=0)
    keyed = d <= TOL
    out = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if keyed[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if keyed[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and keyed[ny, nx] and not out[ny, nx]:
                out[ny, nx] = True; q.append((ny, nx))
    return out

cut = []
for i, fr in enumerate(frames):
    rgb = np.array(fr.convert("RGB")).astype(int)
    bg = alpha_for(rgb)
    arr = np.array(fr)
    arr[..., 3] = np.where(bg, 0, 255)
    cut.append(Image.fromarray(arr, "RGBA"))

# one bounding box for the whole clip, so the bird does not jitter against its own crop
ys, xs = [], []
for c in cut:
    al = np.array(c)[..., 3]
    yy, xx = np.nonzero(al > 8)
    if len(yy): ys += [yy.min(), yy.max()]; xs += [xx.min(), xx.max()]
box = (max(0, min(xs) - 2), max(0, min(ys) - 2), min(w, max(xs) + 3), min(h, max(ys) + 3))
print("crop:", box, "of", (w, h))

sc = TARGET_H / (box[3] - box[1])
size = (round((box[2] - box[0]) * sc), TARGET_H)
# EVERY SECOND FRAME. 156 frames of a 344x460 bird came to 4.6 MB, which is more than the rest of
# the game's art put together for one screen the child sees once. Half the frames at 12fps still
# reads as a smooth cheer - this is a loop of someone bouncing, not a mouth that has to sync.
cut  = cut[::2]
durs = [d * 2 for d in durs[::2]]
out = [c.crop(box).resize(size, Image.LANCZOS) for c in cut]

# PILLOW IN THIS ENVIRONMENT CANNOT WRITE AN ANIMATED WEBP (no SAVE_ALL handler for it), so the
# frames go out as PNGs and ffmpeg assembles them. libwebp_anim keeps the alpha; a GIF here would
# not, and that is the whole point of the exercise.
import subprocess, tempfile, imageio_ffmpeg, shutil
tmp = tempfile.mkdtemp()
for i, f in enumerate(out):
    f.save(os.path.join(tmp, "f%04d.png" % i))
fps = round(1000.0 / (sum(durs) / len(durs)))
FF = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
subprocess.run([FF, "-v", "error", "-y", "-framerate", str(fps),
                "-i", os.path.join(tmp, "f%04d.png"),
                "-loop", "0", "-c:v", "libwebp_anim", "-lossless", "0",
                "-q:v", "62", "-pix_fmt", "yuva420p", OUT], check=True)
shutil.rmtree(tmp, ignore_errors=True)
print("%s  %dx%d  %d frames  %d fps  %.1fs  %d KB"
      % (OUT, size[0], size[1], len(out), fps, len(out) / float(fps), os.path.getsize(OUT) // 1024))
