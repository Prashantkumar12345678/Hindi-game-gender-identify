# HI02H11_L03_S02 — VO MANIFEST (जंगल का मेला)

Generated from the live `card.json`, reconciled against **HI02H11_L03_S02_SME_review** (20-page deck)
and against what is actually present in `assets/Audio/`.

| | |
|---|---|
| Lines to generate | **65** |
| Already present, do not regenerate | 10 |
| Declared but now unused | 1 |
| Deck wording superseded by a later build change | 6 |

Register: Hindi, warm and unhurried, polite *aap* throughout (the deck's own register).
Save each as `assets/Audio/<id>.ogg`.

> Human VO only — `human_vo_check.py` and `no_tts_standard.py` reject synthetic takes. A missing
> clip is SILENT by design; the game plays fine without it. The deck's own EAR-CHECK note flags
> that the earlier build used Gemini 'Kore' TTS — none of that ships.

---

## ⚠ Where the deck and the current build disagree

The deck is the source of truth for **wording**. These three items changed *after* it was
written, on explicit instruction, so the deck text would now be wrong to record verbatim.

### 1. Six match hints now point the wrong way — RE-WORD BEFORE RECORDING

Deck p18 / p25 put the **masculine** card as the stimulus and had the child tap the feminine
one. The build was later reversed: the child now drags the **feminine** card (left) onto the
**masculine** target (right). Each deck line still names the card being dragged *from*.

| id | deck text (p18 / p25) | record THIS instead |
|---|---|---|
| `vo_h2_bail` | यह बैल है, इसे गाय से मिलाएंगे। गाय की तसवीर पर टैप कीजिए। | यह गाय है, इसे बैल से मिलाएंगे। बैल की तसवीर पर टैप कीजिए। |
| `vo_h2_bakra` | यह बकरा है, इसे बकरी से मिलाएंगे। बकरी की तसवीर पर टैप कीजिए। | यह बकरी है, इसे बकरा से मिलाएंगे। बकरा की तसवीर पर टैप कीजिए। |
| `vo_h2_bandar` | यह बंदर है, इसे बंदरिया से मिलाएंगे। बंदरिया की तसवीर पर टैप कीजिए। | यह बंदरिया है, इसे बंदर से मिलाएंगे। बंदर की तसवीर पर टैप कीजिए। |
| `vo_h2_ghoda_p` | यह घोड़ा है, इसे घोड़ी से मिलाएंगे। घोड़ी की तसवीर पर टैप कीजिए। | यह घोड़ी है, इसे घोड़ा से मिलाएंगे। घोड़ा की तसवीर पर टैप कीजिए। |
| `vo_h2_mor_p` | यह मोर है, इसे मोरनी से मिलाएंगे। मोरनी की तसवीर पर टैप कीजिए। | यह मोरनी है, इसे मोर से मिलाएंगे। मोर की तसवीर पर टैप कीजिए। |
| `vo_h2_murga` | यह मुर्गा है, इसे मुर्गी से मिलाएंगे। मुर्गी की तसवीर पर टैप कीजिए। | यह मुर्गी है, इसे मुर्गा से मिलाएंगे। मुर्गा की तसवीर पर टैप कीजिए। |

### 2. `vo_bridge_lost` — DO NOT RECORD

Deck p13 asks for a Swiftee bridge slide after the poem (*"क्या आपको कविता सुनकर मज़ा आया?…"*).
That slide (T10) was later removed from the lesson. The line stays in `card.json` for the
factory, but nothing plays it.

### 3. Deck p22 typo — already corrected in the build, no VO impact

p22 lists *"Correct answer- शेर"* for the बैल slide, but its options are गाय / मोरनी / शेरनी and
its own Hint 2 says गाय. The build has **गाय** correct. Recording is unaffected; noted so the
deck is not treated as authoritative on that line.

---

## To generate (65)

| # | id | slide | deck | line |
|---|---|---|---|---|
| 1 | `vo_c_sentence` | P2 | p23 | शाबाश! सही वाक्य है— बकरा घास खा रहा है। |
| 2 | `vo_correct_pair` | G1, G2, G3, G4, P1 | p14, p15, p16, p17, p22 | शाबाश! आपने सही जोड़ी मिला दी। |
| 3 | `vo_correct_pairs` | G6, P3 | p18, p25 | शाबाश! आपने सभी सही जोड़ियाँ मिला दीं। |
| 4 | `vo_gate_done` | P4 | p26 | शाबाश! आपने सभी जानवर सही गेट से मेले में भेज दिए। |
| 5 | `vo_gate_h1` | P4 | p26 | सोचिए इस जानवर के नाम से वाक्य बनाने पर गया आता है या गई? |
| 6 | `vo_gate_rule` | P4 | p26 | यहाँ दो गेट हैं, एक पर गया लिखा है और दूसरे पर गई लिखा है। हर जानवर के नाम से वाक्य बनाकर देखिए — जिनके अंत में गया आता है उन्हें गया वाले गेट से और जिनके अंत में गई आता है उन्हें गई वाले गेट से मेले में भेजिए। जैसे— मुर्गा मेले में गया। इसे गया वाले गेट से भेजिए। अब आप खुद करिए। |
| 7 | `vo_h1_bail` | P1 | p22 | सोचिए बैल मेले में किसके साथ आया था? |
| 8 | `vo_h1_mor` | G2 | p15 | सोचिए मोर मेले में किसके साथ आया था? |
| 9 | `vo_h1_pair` | G6, P3 | p18, p25 | फिर से कोशिश कीजिए, सही जोड़ी पहचानिए। |
| 10 | `vo_h1_sentence` | P2 | p23 | हम वाक्य में बोलते हैं— बकरा घास खा रहा है। रहा है पर टैप कीजिए और वाक्य पूरा कीजिए। |
| 11 | `vo_h1_sherni` | G1 | p14 | सोचिए शेरनी मेले में किसके साथ आई थी? |
| 12 | `vo_h1_word` | G3, G4 | p16, p17 | फिर से कोशिश कीजिए, सही शब्द पहचानिए। |
| 13 | `vo_h2_bail` | G6 | p18 | यह बैल है, इसे गाय से मिलाएंगे। गाय की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 14 | `vo_h2_bail_gaay` | P1 | p22 | बैल मेले में गाय के साथ आया था। गाय की तस्वीर पर टैप कीजिए। |
| 15 | `vo_h2_bail_jata` | G5 | p19 | यह बैल है, बैल जाता है। इसे जाता है वाले डब्बे में रखेंगे। |
| 16 | `vo_h2_bakra` | P3 | p25 | यह बकरा है, इसे बकरी से मिलाएंगे। बकरी की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 17 | `vo_h2_bakri` | G3 | p16 | यह बकरा है, बकरी-बकरे के साथ मेले में आई थी, इसपर टैप कीजिए। |
| 18 | `vo_h2_bandar` | G6 | p18 | यह बंदर है, इसे बंदरिया से मिलाएंगे। बंदरिया की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 19 | `vo_h2_bandar_gaya` | P4 | p26 | यह बंदर है, बंदर मेले में गया। इसे गया वाले गेट से अंदर भेजेंगे। |
| 20 | `vo_h2_bandariya_gai` | P4 | p26 | यह बंदरिया है, बंदरिया मेले में गई। इसे गई वाले गेट से अंदर भेजेंगे। |
| 21 | `vo_h2_gaay_jati` | G5 | p19 | यह गाय है, गाय जाती है। इसे जाती है वाले डब्बे में रखेंगे। |
| 22 | `vo_h2_ghoda` | G4 | p17 | यह घोड़ी है, घोड़ा-घोड़ी के साथ मेले में आया था, इसपर टैप कीजिए। |
| 23 | `vo_h2_ghoda_p` | P3 | p25 | यह घोड़ा है, इसे घोड़ी से मिलाएंगे। घोड़ी की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 24 | `vo_h2_mor` | G2 | p15 | मोर मेले में मोरनी के साथ आया था। मोरनी की तस्वीर पर टैप कीजिए। |
| 25 | `vo_h2_mor_p` | P3 | p25 | यह मोर है, इसे मोरनी से मिलाएंगे। मोरनी की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 26 | `vo_h2_murga` | G6 | p18 | यह मुर्गा है, इसे मुर्गी से मिलाएंगे। मुर्गी की तसवीर पर टैप कीजिए। ⚠ **re-word, see §1** |
| 27 | `vo_h2_murga_gaya` | P4 | p26 | यह मुर्गा है, मुर्गा मेले में गया। इसे गया वाले गेट से अंदर भेजेंगे। |
| 28 | `vo_h2_murga_jata` | G5 | p19 | यह मुर्गा है, मुर्गा जाता है। इसे जाता है वाले डब्बे में रखेंगे। |
| 29 | `vo_h2_murgi_gai` | P4 | p26 | यह मुर्गी है, मुर्गी मेले में गई। इसे गई वाले गेट से अंदर भेजेंगे। |
| 30 | `vo_h2_murgi_jati` | G5 | p19 | यह मुर्गी है, मुर्गी जाती है। इसे जाती है वाले डब्बे में रखेंगे। |
| 31 | `vo_h2_sher_jata` | G5 | p19 | यह शेर है, शेर जाता है। इसे जाता है वाले डब्बे में रखेंगे। |
| 32 | `vo_h2_sherni` | G1 | p14 | शेरनी मेले में शेर के साथ आई थी। शेर की तस्वीर पर टैप कीजिए। |
| 33 | `vo_h2_sherni_jati` | G5 | p19 | यह शेरनी है, शेरनी जाती है। इसे जाती है वाले डब्बे में रखेंगे। |
| 34 | `vo_match_pairs` | G6, P3 | p18, p25 | सही जोड़ियाँ मिलाइए। |
| 35 | `vo_name_bail` | G1, G3, G5, G6 | p14, p16, p18, p19 | बैल |
| 36 | `vo_name_bakra` | G3, P2, P3 | p16, p23, p25 | बकरा |
| 37 | `vo_name_bandar` | G6, P4 | p18, p26 | बंदर |
| 38 | `vo_name_bandariya` | G2, G6, P4 | p15, p18, p26 | बंदरिया |
| 39 | `vo_name_gaay` | G4, G5, G6, P1 | p17, p18, p19, p22 | गाय |
| 40 | `vo_name_ghoda` | G1, P3 | p14, p25 | घोड़ा |
| 41 | `vo_name_mor` | P3 | p25 | मोर |
| 42 | `vo_poem_01` | T1 | p4 | आइए आज हम एक कविता सुनते हैं— जंगल का मेला। जंगल में एक मेला आया, रंग-बिरंगा खूब सजाया। |
| 43 | `vo_poem_02` | T2 | p5 | शेर आया, शेरनी आई, दोनों ने मिलकर धूम मचाई। |
| 44 | `vo_poem_03` | T3 | p6 | मोर पंख रंगीन फैलाए, मोरनी संग ठुमके लगाए। |
| 45 | `vo_poem_04` | T4 | p7 | घोड़ा आया धूल उड़ाए, घोड़ी पीछे दौड़ी आए। |
| 46 | `vo_poem_05` | T5 | p8 | बकरा बोला— “में-में-में!” बकरी बोली— “साथ चलें!” |
| 47 | `vo_poem_06` | T6 | p9 | बंदर लाया लाल गुब्बारा, बंदरिया बोली कितना प्यारा! |
| 48 | `vo_poem_07` | T7 | p10 | मुर्गा बोला— “कुकड़ू-कूँ!” मुर्गी बोली— “क्या खाऊँ!” |
| 49 | `vo_poem_08` | T8 | p11 | बैल ने जब ढोल बजाया, गाय ने भी नाच दिखाया। |
| 50 | `vo_poem_09` | T9 | p12 | सूरज ढलते शाम हुई, मेले भर में धूम हुई। |
| 51 | `vo_pt_guided` | (gate) | p3 | बहुत बढ़िया! अब हम साथ मिलकर शुरू करते हैं। चलिए, साथ में करें! |
| 52 | `vo_pt_practice` | (gate) | p3 | वाह! अब आपकी बारी। |
| 53 | `vo_pt_tutorial` | (gate) | p3 | ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें! |
| 54 | `vo_q_bail` | P1 | p22 | यह बैल है, इसे इसकी सही जोड़ी से मिलाइए। |
| 55 | `vo_q_bakri` | G3 | p16 | यह किसके साथ मेले में आई थी? |
| 56 | `vo_q_ghoda` | G4 | p17 | यह किसके साथ मेले में आया था? |
| 57 | `vo_q_mor` | G2 | p15 | यह मोर है, इसे इसकी सही जोड़ी से मिलाइए। |
| 58 | `vo_q_sentence` | P2 | p23 | सही शब्द चुनकर वाक्य पूरा कीजिए। बकरा घास खा… रहा है या रही है? |
| 59 | `vo_q_sherni` | G1 | p14 | यह शेरनी है, इसे इसकी सही जोड़ी से मिलाइए। |
| 60 | `vo_sort_jata_demo` | G5 | p19 | बैल मेले में जाता है। गाय मेले में जाती है। |
| 61 | `vo_sort_jata_done` | G5 | p19 | शाबाश! आपने सभी जानवर सही डब्बे में रख दिए। |
| 62 | `vo_sort_jata_h1` | G5 | p19 | वाक्य बनाकर देखिए, यह जानवर जाता है या जाती है। |
| 63 | `vo_sort_jata_rule` | G5 | p19 | इसी तरह हर जानवर के शब्द का वाक्य बनाकर देखिए। जिन वाक्यों के अंत में जाता है आता है उन्हें जाता है वाले डब्बे में, और जिन वाक्यों के अंत में जाती है आता है उन्हें जाती है वाले डब्बे में रखिए। |
| 64 | `vo_word_raha_hai` | P2 | p23 | रहा है |
| 65 | `vo_word_rahi_hai` | P2 | p23 | रही है |

---

## Already present — do NOT regenerate

| id | line |
|---|---|
| `vo_landing` | नमस्ते दोस्त! मैं हूँ स्विफ्टी। आइए आज हम शब्दों की जोड़ियाँ बनाते हैं। जैसे— मोर-मोरनी। |
| `vo_name_bakri` | बकरी |
| `vo_name_ghodi` | घोड़ी |
| `vo_name_morni` | मोरनी |
| `vo_name_murga` | मुर्गा |
| `vo_name_murgi` | मुर्गी |
| `vo_name_sher` | शेर |
| `vo_name_sherni` | शेरनी |
| `vo_try_again` | फिर से कोशिश कीजिए। |
| `vo_well_done` | शाबाश! आपने सभी सही जोड़ियाँ पहचान लीं। |

---

## Generate in this order

The lesson is playable but almost entirely silent — 65 of 75 clips are missing.

1. **`vo_poem_01`–`vo_poem_09`** (deck p4–p12) — the whole tutorial T1–T9 *is* the poem. Those
   nine slides have no narration at all right now; the video's own ambience is the only sound.
2. **`vo_pt_tutorial` / `vo_pt_guided` / `vo_pt_practice`** (deck p3) — the three Swiftee
   transition gates. They currently hold on a fixed 3.15s timer instead of following the clip.
3. **`vo_landing`** is already present; **`vo_sort_jata_demo` + `vo_sort_jata_rule`** (deck p19)
   next — G5's worked example runs on fixed beats because there is no clip to sync the hand to.
4. **`vo_gate_rule` + `vo_gate_h1`** (deck p26), then the remaining prompts (`vo_q_*`),
   then the hint ladders (`vo_h1_*`, `vo_h2_*`), then feedback lines.
