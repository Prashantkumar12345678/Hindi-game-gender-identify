# VO MANIFEST — read off the SME review deck

**HI02H11_L03_S02 · लड़का या लड़की? (लिंग पहचानो) · जंगल का मेला**

Every VO line the SME deck writes out, in deck order, transcribed from
`HI02H11_L03_S02_SME_review.pdf` (pages 3–27).

> This file is a **transcription of the deck**. It is not generated from `card.json`,
> and no code or content file was changed to produce it. Where the deck and the current
> build disagree, this file follows **the deck**.

**55 lines.** Save each as `assets/Audio/<id>.ogg`.
Hindi, warm and unhurried, polite *aap* register — the deck's own register.
**Human voice only** — the deck's EAR-CHECK note flags that the earlier build shipped
Gemini "Kore" TTS, and `human_vo_check.py` / `no_tts_standard.py` reject synthetic takes.

---

## Landing & Swiftee transitions

| # | pg | slide | id | line |
|---|----|-------|----|------|
| 1 | p3 | 01_landing | `vo_landing` | नमस्ते दोस्त! मैं हूँ स्विफ्टी, आइए आज हम शब्दों की जोड़ियाँ बनाते हैं। जैसे— मोर-मोरनी। |
| 2 | p3 | Swiftee transition · before Tutorial | `vo_pt_tutorial` | ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें! |
| 3 | p3 | Swiftee transition · before Guided | `vo_pt_guided` | बहुत बढ़िया! अब हम साथ मिलकर शुरू करते हैं। चलिए, साथ में करें! |
| 4 | p3 | Swiftee transition · before Practice | `vo_pt_practice` | वाह! अब आपकी बारी। |

## कविता — जंगल का मेला

| # | pg | slide | id | line |
|---|----|-------|----|------|
| 5 | p4 | poem — lead-in | `vo_poem_intro` | आइए आज हम एक कविता सुनते हैं— जंगल का मेला। |
| 6 | p4 | poem 1 — मेला | `vo_poem_01` | जंगल में एक मेला आया, रंग-बिरंगा खूब सजाया। |
| 7 | p5 | poem 2 — शेर/शेरनी | `vo_poem_02` | शेर आया, शेरनी आई, दोनों ने मिलकर धूम मचाई। |
| 8 | p6 | poem 3 — मोर/मोरनी | `vo_poem_03` | मोर पंख रंगीन फैलाए, मोरनी संग ठुमके लगाए। |
| 9 | p7 | poem 4 — घोड़ा/घोड़ी | `vo_poem_04` | घोड़ा आया धूल उड़ाए, घोड़ी पीछे दौड़ी आए। |
| 10 | p8 | poem 5 — बकरा/बकरी | `vo_poem_05` | बकरा बोला— "में-में-में!" बकरी बोली— "साथ चलें!" |
| 11 | p9 | poem 6 — बंदर/बंदरिया | `vo_poem_06` | बंदर लाया लाल गुब्बारा, बंदरिया बोली कितना प्यारा! |
| 12 | p10 | poem 7 — मुर्गा/मुर्गी | `vo_poem_07` | मुर्गा बोला— "कुकड़ू-कूँ!" मुर्गी बोली— "क्या खाऊँ!" |
| 13 | p11 | poem 8 — बैल/गाय | `vo_poem_08` | बैल ने जब ढोल बजाया, गाय ने भी नाच दिखाया। |
| 14 | p12 | poem 9 — शाम | `vo_poem_09` | सूरज ढलते शाम हुई, मेले भर में धूम हुई। |
| 15 | p13 | Swiftee bridge | `vo_bridge_lost` | क्या आपको कविता सुनकर मज़ा आया? मेले में भीड़ की वजह से सभी जोड़ियाँ बिछड़ गईं। क्या आप सही जोड़ियाँ ढूँढने में मेरी मदद करेंगे? आइए साथ मिलकर ढूँढ़ते हैं। |

## Guided

| # | pg | slide | id | line |
|---|----|-------|----|------|
| 16 | p14 | 06_TAP_GENDER — शेरनी | `vo_q_sherni` | यह शेरनी है, इसे इसकी सही जोड़ी से मिलाइए। |
| 17 | p14 | 06 · Hint 1 | `vo_h1_sherni` | सोचिए शेरनी मेले में किसके साथ आई थी? |
| 18 | p14 | 06 · Hint 2 | `vo_h2_sherni` | शेरनी मेले में शेर के साथ आई थी। शेर की तस्वीर पर टैप कीजिए। |
| 19 | p14 | 06 · correct (shared) | `vo_correct_pair` | शाबाश! आपने सही जोड़ी मिला दी। |
| 20 | p15 | 07_TAP_GENDER — मोर | `vo_q_mor` | यह मोर है, इसे इसकी सही जोड़ी से मिलाइए। |
| 21 | p15 | 07 · Hint 1 | `vo_h1_mor` | सोचिए मोर मेले में किसके साथ आया था? |
| 22 | p15 | 07 · Hint 2 | `vo_h2_mor` | मोर मेले में मोरनी के साथ आया था। मोरनी की तस्वीर पर टैप कीजिए। |
| 23 | p16 | 08_TAP_PICTURE — बकरी | `vo_q_bakri` | यह किसके साथ मेले में आई थी? बकरी |
| 24 | p16 | 08 · Hint 1 (shared) | `vo_h1_word` | फिर से कोशिश कीजिए, सही शब्द पहचानिए। |
| 25 | p16 | 08 · Hint 2 | `vo_h2_bakri` | यह बकरा है, बकरी-बकरे के साथ मेले में आई थी, इसपर टैप कीजिए। |
| 26 | p17 | 09_TAP_PICTURE — घोड़ा | `vo_q_ghoda` | यह किसके साथ मेले में आया था? घोड़ा |
| 27 | p17 | 09 · Hint 2 | `vo_h2_ghoda` | यह घोड़ी है, घोड़ा-घोड़ी के साथ मेले में आया था, इसपर टैप कीजिए। |
| 28 | p18 | 11_MATCH · Hint 1 | `vo_h1_pair` | फिर से कोशिश कीजिए, सही जोड़ी पहचानिए। |
| 29 | p18 | 11_MATCH · Hint 2 | `vo_h2_bandar` | यह बंदर है, इसे बंदरिया से मिलाएंगे। बंदरिया की तसवीर पर टैप कीजिए। |
| 30 | p18 | 11_MATCH · Hint 2 | `vo_h2_murga` | यह मुर्गा है, इसे मुर्गी से मिलाएंगे। मुर्गी की तसवीर पर टैप कीजिए। |
| 31 | p18 | 11_MATCH · Hint 2 | `vo_h2_bail` | यह बैल है, इसे गाय से मिलाएंगे। गाय की तसवीर पर टैप कीजिए। |
| 32 | p18 | 11_MATCH · correct (shared) | `vo_correct_pairs` | शाबाश! आपने सभी सही जोड़ियाँ मिला दीं। |
| 33 | p19 | 10_SORT · demo | `vo_sort_jata_demo` | बैल मेले में जाता है। गाय मेले में जाती है। |
| 34 | p19 | 10_SORT · rule | `vo_sort_jata_rule` | इसी तरह हर जानवर के शब्द का वाक्य बनाकर देखिए, जिन वाक्यों के अंत में जाता है आता है उन्हें जाता है वाले डब्बे में और जिन वाक्यों के अंत में जाती है आता है उन्हें जाती है वाले डब्बे में रखिए। |
| 35 | p19 | 10_SORT · Hint 1 | `vo_sort_jata_h1` | वाक्य बनाकर देखिए, यह जानवर जाता है या जाती है। |
| 36 | p19 | 10_SORT · Hint 2 | `vo_h2_sher_jata` | यह शेर है, शेर जाता है। इसे जाता है वाले डब्बे में रखेंगे। |
| 37 | p19 | 10_SORT · Hint 2 | `vo_h2_sherni_jati` | यह शेरनी है, शेरनी जाती है। इसे जाती है वाले डब्बे में रखेंगे। |
| 38 | p19 | 10_SORT · Hint 2 | `vo_h2_murga_jata` | यह मुर्गा है, मुर्गा जाता है। इसे जाता है वाले डब्बे में रखेंगे। |
| 39 | p19 | 10_SORT · Hint 2 | `vo_h2_murgi_jati` | यह मुर्गी है, मुर्गी जाती है। इसे जाती है वाले डब्बे में रखेंगे। |

## Practice

| # | pg | slide | id | line |
|---|----|-------|----|------|
| 40 | p22 | 18_TAP_GENDER — बैल | `vo_q_bail` | यह बैल है, इसे इसकी सही जोड़ी से मिलाइए। |
| 41 | p22 | 18 · Hint 1 | `vo_h1_bail` | सोचिए बैल मेले में किसके साथ आया था? |
| 42 | p22 | 18 · Hint 2 | `vo_h2_bail_gaay` | बैल मेले में गाय के साथ आया था। गाय की तस्वीर पर टैप कीजिए। |
| 43 | p23 | 16_TAP_GENDER — वाक्य | `vo_q_sentence` | सही शब्द चुनकर वाक्य पूरा कीजिए। बकरा घास खा… रहा है या रही है? |
| 44 | p23 | 16 · Hint 1 | `vo_h1_sentence` | हम वाक्य में बोलते हैं— बकरा घास खा रहा है। रहा है पर टैप कीजिए और वाक्य पूरा कीजिए। |
| 45 | p23 | 16 · correct | `vo_c_sentence` | शाबाश! सही वाक्य है— बकरा घास खा रहा है। |
| 46 | p25 | 14_MATCH · Hint 2 | `vo_h2_bakra` | यह बकरा है, इसे बकरी से मिलाएंगे। बकरी की तसवीर पर टैप कीजिए। |
| 47 | p25 | 14_MATCH · Hint 2 | `vo_h2_mor_p` | यह मोर है, इसे मोरनी से मिलाएंगे। मोरनी की तसवीर पर टैप कीजिए। |
| 48 | p25 | 14_MATCH · Hint 2 | `vo_h2_ghoda_p` | यह घोड़ा है, इसे घोड़ी से मिलाएंगे। घोड़ी की तसवीर पर टैप कीजिए। |
| 49 | p26 | 15_SORT (gates) · rule | `vo_gate_rule` | यहाँ दो गेट हैं, एक पर गया लिखा है और दूसरे पर गई लिखा है। हर जानवर के नाम से वाक्य बनाकर देखिए — जिनके अंत में गया आता है उन्हें गया वाले गेट से और जिनके अंत में गई आता है उन्हें गई वाले गेट से मेले में भेजिए। जैसे— मुर्गा मेले में गया। इसे गया वाले गेट से भेजिए। अब आप खुद करिए। |
| 50 | p26 | 15_SORT · Hint 1 | `vo_gate_h1` | सोचिए इस जानवर के नाम से वाक्य बनाने पर गया आता है या गई? |
| 51 | p26 | 15_SORT · Hint 2 | `vo_h2_bandar_gaya` | यह बंदर है, बंदर मेले में गया। इसे गया वाले गेट से अंदर भेजेंगे। |
| 52 | p26 | 15_SORT · Hint 2 | `vo_h2_bandariya_gai` | यह बंदरिया है, बंदरिया मेले में गई। इसे गई वाले गेट से अंदर भेजेंगे। |
| 53 | p26 | 15_SORT · Hint 2 | `vo_h2_murga_gaya` | यह मुर्गा है, मुर्गा मेले में गया। इसे गया वाले गेट से अंदर भेजेंगे। |
| 54 | p26 | 15_SORT · Hint 2 | `vo_h2_murgi_gai` | यह मुर्गी है, मुर्गी मेले में गई। इसे गई वाले गेट से अंदर भेजेंगे। |

## Celebration

| # | pg | slide | id | line |
|---|----|-------|----|------|
| 55 | p27 | 19_CELEBRATION | `vo_well_done` | शाबाश! आपने सभी सही जोड़ियाँ पहचान लीं। |

---

## What the deck says around the lines

Recorded here because it affects what gets read, not because it is itself a line:

1. **p3 — three Swiftee transition slides.** The deck asks for one before Tutorial, one
   before Guided, one before Practice, each with its own line (rows 2–4). It also notes
   *"शुरू करें पर hand nudge नहीं आएगा"* and *"Swiftee के पैर पर audio बटन आएगा"*.

2. **p4 — the poem's lead-in is written separately.** Row 5 (*"आइए आज हम एक कविता सुनते हैं—
   जंगल का मेला।"*) sits above verse 1 on the same page, with a *change image* note between
   them. Record it as its own clip; the deck does not say to join it to verse 1.

3. **p4–p12 — the poem is one continuous recitation** in nine verses. Keep one voice, one
   tempo and one rhyme-landing across all nine, and record them in a single session.

4. **p14–p18 — "Hint 2 बताते हुए hand nudge आएगा guided section में।"** Highlighted on five
   pages. Behaviour note; nothing to record.

5. **p19 — "इस VO के साथ-साथ बैल और गाय को सही डब्बे में डालकर दिखाना है।"** The demo placement
   animates *with* row 33, so that clip's pacing drives it. Leave a clear beat after each
   of the two sentences.

6. **p20, p21, p24 — "delete slide."** Three slides marked for removal. No VO.

7. **p22 — a slip in the deck.** It prints *"Correct answer- शेर"* for the बैल slide, but the
   options are गाय / मोरनी / शेरनी and its own Hint 2 (row 42) says गाय. गाय is right; the
   recording is unaffected.

8. **p16, p17 — placeholder text.** *"जहाँ स्त्रीलिंग लिखा है वहाँ बकरी/घोड़ा लिखना है।"* An
   on-screen text fix, not VO.

9. **Not written out in the deck.** The per-option word clips and the generic retry line have
   no text in the deck. p14–p17 say *"options एक-एक करके screen पर आने चाहिए with VO"*, which
   implies a short clip per option (शेर, बैल, घोड़ा, मोरनी, मुर्गी, बंदरिया …), but the deck
   never writes those words, so they are not counted in the 55 above. Confirm with the SME
   before recording them.
