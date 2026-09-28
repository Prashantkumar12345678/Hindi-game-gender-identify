SwiftPAL round play button
==========================

  play-round.svg           gold, ready
  play-round-waiting.svg   grey, not yet tappable

Both are 116 x 116. The file is padded 14px on every side so the drop shadow is
not clipped, so the DISC a child sees is about 75% of whatever box you give it:
at width:190px the disc is ~143px, at 140px it is ~105px.

Colours
  gold face   #FFD24E -> #FCB717 -> #F2A80F (top to bottom)
  gold side   #D98F06
  rim         #FFFFFF
  triangle    #0B3D8C
  grey face   #E9E9EE -> #D8D8DF -> #C6C6CE
  grey side   #A8A8B2
  grey glyph  #8B8B95

Three ways to use it

  1. as an image
       <img src="play-round.svg" alt="Play" width="140">

  2. as a CSS background, which is how the game does it - it lets one
     element swap between the two states without touching the markup:
       .play-btn        { width:140px; height:140px; border:0; padding:0;
                          background:transparent url("play-round.svg")
                                     center/140px 140px no-repeat; }
       .play-btn.waiting{ background-image:url("play-round-waiting.svg"); }

  3. inline in the page. The ids inside are prefixed pb- for exactly this:
     inline SVG ids are global to the document, so an unprefixed id="face"
     would collide with anything else on the page that uses that name - and
     the symptom is a gradient silently rendering as black.

Notes
  Self-contained: no fonts, no external files, no CSS needed.
  The triangle is filled AND stroked in its own colour with a round join.
  That is what rounds its corners; a plain filled path cannot, and an outline
  in a different colour reads as a line drawn round the glyph.
  The depth is one rim with the darker gold showing as a 3px crescent inside
  it. A second disc with its own rim reads as two buttons stacked.
