# HI02H11_L03_S02 — "जंगल का मेला" · SME deck applied

Deck: `HI02H11_L03_S02_SME_review.pptx` (Bindu Gupta, 2026-09-14) · 28 deck slides · 20 reviewed pages
**Baseline: MATCHED** — deck slide 2 describes engine `2026.07.10-unified`, 18 slides, 5-phase, which
is exactly the delivered build.

**Receipt, verbatim:** ` 17 pass · 3 FAIL · 6 warn `
All three FAILs are the un-produced assets (below) and the "silent prompts" that follow from them.
Nothing else is red. `render_check --scope kg` : **24 slides, 0 broken, 0 console errors.**
`attempts_check` : **OK — 3 with a full hint2 ladder (10/10 answerable slides).**

Status enum: ✅ DONE · ⚑ FLAGGED · ⏳ BLOCKED · N/C (nothing requested)

---

## What the lesson is now

**24 slides on the 3-phase contract** (was 18 on the old 5-phase arc):

| Phase | Slides |
|---|---|
| tutorial (11) | journey gate → **9 poem beats** (`STORY_SCENE`, full-bleed) → the "pairs got separated" beat |
| guided (7) | gate → 4 pair-finding questions → sort into **जाता है / जाती है** → match 3 pairs |
| practice (6) | gate → match 3 pairs → the two **गया / गई** मेला gates → complete the sentence → बैल's pair → celebration |

---

## A · Landing + journey (deck slide 3)

| # | Change (verbatim) | Status | Proof |
|---|---|---|---|
| 1 | heading text- आइए जोड़ी मिलाएं | ✅ | `card.title.hi`; shot `01_landing.png` |
| 2 | Image - एक मोर और एक मोरनी का चित्र | ✅ wired / ⏳ art | `landing_hero.concept_strip` = pic_mor + pic_morni with labels; art pending |
| 3 | Vo- नमस्ते दोस्त! … जैसे- मोर-मोरनी | ✅ text / ⏳ clip | `vo_landing` re-texted; recording pending |
| 4 | शुरू करे पर hand nudge नहीं आएगा | ✅ | already true on this engine — **no nudge targets `#sgBtn` at all**; verified by sweep |
| 5 | Swiftee के पैर पर audio बटन आएगा | ✅ | engine renders the chip on the mascot's shoulder/foot; shot `01_landing.png` |
| 6 | Add swiftee transition slide | ✅ | 3 × `PHASE_TRANSITION` (`PT_TUT`, `PT_GUI`, `PT_PRA`); shots 02, 13, 20 |
| 7–9 | the three gate VO lines, verbatim | ✅ text / ⏳ clips | `vo_pt_tutorial` / `vo_pt_guided` / `vo_pt_practice`, registered word-for-word |

## B · जंगल का मेला — the poem (deck slides 4–13)

All nine beats built as `STORY_SCENE`, heading **जंगल का मेला**, one verse each, **full-bleed and
travelling** (see E1). Shots `03`–`11`; the bridge beat is shot `12`.

| # | Beat | VO id | Status |
|---|---|---|---|
| 10 | मेला opens | `vo_poem_01` | ✅ built · ⏳ art+VO |
| 11 | शेर + शेरनी *(deck asked "animation के साथ")* | `vo_poem_02` | ✅ built · ⏳ art+VO |
| 12 | मोर + मोरनी | `vo_poem_03` | ✅ · ⏳ |
| 13 | घोड़ा + घोड़ी | `vo_poem_04` | ✅ · ⏳ |
| 14 | बकरा + बकरी, with the two speech bubbles | `vo_poem_05` | ✅ (`caption_hi` carries "में-में-में!" / "साथ चलें!") · ⏳ |
| 15 | बंदर + बंदरिया + balloon + भालू | `vo_poem_06` | ✅ · ⏳ |
| 16 | मुर्गा + मुर्गी | `vo_poem_07` | ✅ · ⏳ |
| 17 | बैल + गाय | `vo_poem_08` | ✅ · ⏳ — **ruling applied, see F1** |
| 18 | सब जोड़ियाँ, शाम | `vo_poem_09` | ✅ · ⏳ |
| 19 | "सभी जोड़ियाँ बिछड़ गईं" bridge | `vo_bridge_lost` | ✅ built as a 4th transition beat |

## C · Guided (deck slides 14–17) — shots 14–17

| # | Change | Status |
|---|---|---|
| 20–21 | pg6 heading **सही जोड़ी से मिलाइए।** + VO यह शेरनी है… | ✅ |
| 22 | pg6 stimulus शेरनी alone at the fair | ✅ wired (`pic_sherni_alone`) · ⏳ art |
| 23 | **options one by one with VO** | ✅ `data.reveal_seq` on every question |
| 24 | pg6 3 options बैल · शेर · घोड़ा, **picture + name**, correct **शेर** | ✅ |
| 25 | pg6 Hint 1 + Hint 2, verbatim | ✅ `audio.hint1` / `audio.hint2` |
| 26 | hand nudge on Hint 2, guided only | ✅ engine `handOnAnswer` is phase-gated to tutorial+guided |
| 27 | correct VO शाबाश! आपने सही जोड़ी मिला दी। | ✅ |
| 28 | pg7 मोर → मोरनी (मोरनी · मुर्गी · बंदरिया) + both hints | ✅ |
| 29 | pg8 **सही तसवीर चुनिए।**, stimulus reads **बकरी** not "स्त्रीलिंग", options शेरनी · बकरा · बैल, correct **बकरा** | ✅ (needed engine edit E5) |
| 30 | pg9 stimulus reads **घोड़ा**, options मुर्गी · गाय · घोड़ी, correct **घोड़ी** | ✅ |

## D · The sorts and matches (deck slides 18, 19, 25, 26) — shots 18, 19, 21, 22

| # | Change | Status |
|---|---|---|
| 31 | pg11 सही जोड़ियाँ मिलाइए। · बंदरिया-मुर्गी-गाय / बैल-बंदर-मुर्गा | ✅ |
| 32 | pg11 Hint 1 + **a different Hint 2 per pair** + nudge | ✅ (needed engine edit E1) |
| 33 | pg10 **Box 1 जाता है। / Box 2 जाती है।** (was पुल्लिंग/स्त्रीलिंग) | ✅ — bin labels are free text, matching keys off `gender` |
| 34 | pg10 items शेर-शेरनी, मुर्गा-मुर्गी, बैल-गाय | ✅ |
| 35 | pg10 worked example: **बैल and गाय place themselves** as the demo VO plays | ✅ (engine edit E2) — ⚑ see F5 |
| 36 | pg10 rule VO | ✅ `audio.instruction`, plays after the demo |
| 37 | pg10 Hint 1 + per-item Hint 2 (शेर/शेरनी/मुर्गा/मुर्गी) | ✅ |
| 38 | pg14 बकरा-बकरी · मोर-मोरनी · घोड़ा-घोड़ी + 3 × Hint 2 | ✅ |
| 39 | pg15 **हर जानवर को सही गेट से…**, Box 1 **गया।** / Box 2 **गई।**, drawn as **two मेला gates** | ✅ (engine edit E3) |
| 40 | pg15 items बंदर-बंदरिया, मुर्गा-मुर्गी | ✅ |
| 41 | pg15 rule + worked-example VO, Hint 1 + 4 × Hint 2 | ✅ |

## E · Mastery, celebration, deletes (deck slides 20–24, 27)

| # | Change | Status |
|---|---|---|
| 42 | pg12 (I3) **delete** | ✅ deleted by ID |
| 43 | pg13 (I4) **delete** | ✅ deleted by ID |
| 44 | pg17 (M2) **delete** | ✅ deleted by ID |
| 45 | pg18 बैल → **गाय**, 3 options | ✅ — **ruling applied, see F2** |
| 46 | pg16 **वाक्य पूरा कीजिए।** — बकरा घास खा… रहा है / रही है, correct **रहा है** | ✅ shot `23` |
| 47 | pg19 celebration, **only VO, no text** | ✅ engine [30i] already renders it text-free; `prompt_hi` blanked |
| 48 | pg20 `_deck_A.jpg` — "• —" | **N/C** |

---

## ⚑ RULINGS TAKEN (you decided these on 2026-09-14)

**F1 · Poem beat 8** — deck slide 11's image note said हाथी/हथिनी, its own VO says बैल/गाय.
→ **बैल + गाय**, per the VO. Consistent with pages 10, 11 and 18; हाथी appears nowhere else.

**F2 · Mastery बैल (deck slide 22)** — said "2 options" while listing three, and "Correct answer- शेर"
while शेर was not an option and its own Hint 2 named गाय. → **3 options, correct = गाय.**

**F3 · Pages 3–5 (T2/T3/T4)** carried no note. → **the poem replaces the tutorial**; the three
लड़का/लड़की/शेरनी MEET_GENDER slides are gone. Their clips are quarantined, not deleted.

**F4 · Register** flips informal *tum* → polite *aap* across the whole deck. Adopted throughout, per
the one-register-per-game rule. Flagging, not asking.

**F5 · The worked example vs. a house rule.** The house rule is "no question is solved automatically
in guided/practice". Deck page 10 explicitly asks for बैल and गाय to be placed *for* the child as the
demo speaks. Built as asked: those two are a demonstration, the remaining four stay the child's.
**Raised for the lead**, not resolved by me.

**F6 · The teaching target widens.** Pages 10/15/16 no longer test पुल्लिंग/स्त्रीलिंग but **verb
agreement** (जाता है/जाती है, गया/गई, रहा है/रही है). Richer, and arguably better — but broader than
LO `HI02H11_L03` as catalogued. **Needs curriculum sign-off.** Implemented as asked.

---

## 🔑 BLOCKED — the two things I could not produce here

**A1 · 17 images.** 9 जंगल का मेला poem scenes + 8 picture chips. Brief is written and
**ready to run**: `_handoff/ART_BRIEF.json`, art-directed to match `HIKGH01_L02_S03` ("कहानी — तोता"),
the reference you named — warm painted storybook, soft brown outlines, golden light, wide 16:9.
Needs `GEMINI_KEY` in the environment, which is not set on this machine:
```
$env:GEMINI_KEY = "AIza..."
PYTHONUTF8=1 python <skill>/scripts/build/gen_scenes.py  KG/HI02H11_L03_S02/assets/Images --manifest KG/HI02H11_L03_S02/_handoff/ART_BRIEF.json
PYTHONUTF8=1 python <skill>/scripts/build/gen_objects.py KG/HI02H11_L03_S02/assets/Images --manifest <objects half>
```
Run `sc_mela_01` first — every later scene references it to hold the fair's look steady.
Until then each scene falls back to its emoji, which is why the art gate is red.

**A2 · 67 voice clips.** `_handoff/VO_RECORDING_LIST.md`, every line written out, id by id.
**Not synthesisable:** the ship gate is explicit (`human_vo_check.py`, Yasir 2026-08-08 — "only human
VO is to be used") and `no_tts_standard.py` forbids any synthetic fallback. A missing clip is silent
**by design**, so the game builds and plays now and simply gains its voice when the takes land.

---

## 🔧 ENGINE — isolated, additive, 12 edits

The game is **isolated** (`engine_local/`, seeded from `2026.08.04b-r4-unified`, stamp + sha in
`_baseline.json`). Forced, not chosen: this kit ships no `factories/Maths HTML Factory/engine/app.js`,
so `unified_build`'s content-sync guard is unverifiable and **fails closed for every FLN build in the
kit — the two reference games included**. Trade-off: this game will not auto-receive later fleet fixes.
All edits are reproducible via `scripts/patch_engine_HI02H11_L03_S02.py` (idempotent, re-runnable).

| id | Edit | Why |
|---|---|---|
| E1 | per-item rung-2 on **picture** tiles | [25b]'s lookup matched `tile.textContent` against `pairs[].letter` — right for letter tiles, unreachable for a picture sort. And `SORT_GENDER`/`MATCH_GENDER_PAIRS` never passed their tile at all, so an authored per-item hint could not fire. |
| E2 | `SORT_GENDER data.demo_items` | the pg10 worked example |
| E3 | `SORT_GENDER data.gates` | pg15's two मेला gates (skin only, scoped) |
| E4 | `STORY_QUESTION data.stim_word_hi` | pg8/pg9 "जहां स्त्रीलिंग लिखा है वहाँ बकरी लिखना है" — the stimulus had no label at all |
| E5 | real recorded SFX | FLN Animation Kit recipe 22 — replaces the engine's Web Audio tones with four real recordings |
| E6 | full-bleed travelling `STORY_SCENE` | your direction: the मेला fills the screen and travels |
| E6b | mascot un-clipped in full-bleed | caught in the capture walk — her feet were cut off |

**⚑ E6 knowingly overrides two standing rulings, for opted-in slides only:** [27i] "teaching images
carry no container / object-fit contain" and [28d] "the STORY_SCENE picture must stay completely
still". Both still hold everywhere `data.full_bleed` is absent — every other slide here, and every
slide in every other game. [28d]'s `!important` is beaten by specificity, not removed, so deleting the
opt-in restores it exactly. `prefers-reduced-motion` still stops the travel. **Raised for the lead.**

**Sibling regression:** N/A — no shared-engine file was touched. Every edit is inside this game's
private `engine_local/`.

---

## CHANGED BEYOND THE DECK

* **Migration to the current engine + 3-phase fold.** Required by `migration_playbook.md` before any
  feedback may be applied. It is also what makes most of this deck cheap — `reveal_seq`, the
  hint1/hint2 ladder, the guided-only hand, `STORY_SCENE` and `PHASE_TRANSITION` all already existed
  there and would have had to be built from scratch on the old engine.
* **`audio.hint2` added alongside `audio.hint`** on the pick slides. Real fix, not cosmetic: `midHint()`
  reads `hint2` first, and the attempts gate counts only `hint2` — it read the ladder as 4/10 before
  and 10/10 after.
* **UI chrome kit copied from `HI01H04_L03_S04`.** `unified_build` found no kit and copied **zero**
  files. The delivered bundle carries the old `sw_anim_*.gif` chrome while this engine's mascot is the
  21a expression heads (`sw_head_*.webp`) — without them `setSwMood()` paints nothing.
* **Four real SFX + their licence** (E5), and **15 superseded clips quarantined** to
  `assets/Audio/_superseded_2026-09-14/` — moved, never deleted, per the kit rule.
* **Hand-off docs live in `_handoff/`**, outside `assets/`, so they are never read as shippable assets.

## Observations — noticed, NOT changed

* **The kit is missing `factories/Maths HTML Factory/engine/app.js` and `style.css`.** Every FLN build
  in it refuses to run, the two QA reference games included. Worth fixing at the kit level; isolation
  is a workaround, not a repair.
* **`intake_triage.py` and `engine_isolate.py` carry hard-coded `C:/Users/yali6/...` paths** and crash
  on any other machine. `engine_local/_build_isolated.py` in the reference bundles has the same.
* **`attempts_check` cannot see per-item `hint2`** in `items[]`/`pairs[]`… it can, and does — but only
  the field named exactly `hint2`. Worth documenting, since `hint2_audio` is the older spelling.
* **`HI01H04_L02_S01` fails the attempts ruling** (max 3, hint2 on 2/7). Pre-existing, not this run.
* **Deck page 16's "Hint 1" already gives the answer** ("रहा है पर टैप कीजिए"), so rung 2 has nothing
  left to escalate to and repeats it. Built as written.
* **बकरा/बकरी and मोर/मोरनी are visually similar pairs.** The word label under each picture carries the
  distinction. Worth an eye once the art exists.
