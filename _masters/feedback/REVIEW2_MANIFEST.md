# Review 2 — manifest

**Game:** HI02H11_L03_S02 · आइए जोड़ी मिलाएँ
**Source:** `_masters/feedback/Feedback_Review1-3.pdf`, pages 5–10 (Review 2 section only)
**Checked against the build on:** 2026-09-28

Har Review 2 item yahan hai — deck kya kehta hai, build mein kahan gaya, aur ab kya baaki hai.
Status teen hi hain:

| | |
|---|---|
| **✅ DONE** | build mein hai aur chal raha hai |
| **🎙️ VO PENDING** | screen ban gayi, sirf recording baaki — id authored hai, file nahi |
| **⬜ OPEN** | abhi kiya nahi gaya |

---

## 1. Landing screen (deck p. 6)

| # | Review 2 kehta hai | Status | Note |
|---|---|---|---|
| 1.1 | Title → **जोड़ी मिलाइए** | ⬜ OPEN | Abhi `आइए जोड़ी मिलाएँ` hai — title text aur landing ke beech wali title image (`title.png`) dono badalni hongi |
| 1.2 | VO → "नमस्ते दोस्त, मैं हूँ swiftee, आज हम शब्दों की जोड़ियाँ मिलाएंगे।" | ⬜ OPEN | Nayi recording chahiye |
| 1.3 | **Remove speaker button** | ⬜ OPEN | `.sg-vo` abhi landing par hai |
| 1.4 | **Increase size of mor-morni** | ⬜ OPEN — **conflict** | Review 2 bada karne ko kehta hai; baad mein "मोर and मोरनी ka photo thoda chota karo" bola gaya tha aur chhota kiya gaya. **Ek ruling chahiye** — kaunsa chalega |

## 2. कविता — जंगल का मेला (deck p. 6–7)

| # | Review 2 kehta hai | Status | Note |
|---|---|---|---|
| 2.1 | जंगल में एक मेला आया, / रंग-बिरंगा खूब सजाया। | ✅ DONE | T1 pehle se aisa hi tha |
| 2.2 | मुर्गा बोला, "कुकड़ू-कूँ" / मुर्गी बोली, "क्या खाऊँ?" | ✅ DONE | T7 — dash → comma, `!` → `?` |
| 2.3 | बकरा बोला, "में-में-में" / बकरी बोली, "साथ चले।" | ✅ DONE | T5 — "चलें" → "चले" bhi |
| 2.4 | बंदर लाया लाल गुब्बारा, / बंदरिया बोली, "कितना प्यारा।" | ✅ DONE | T6 — quotes add hue |
| 2.5 | **Change image of murgi** | ⬜ OPEN — **holding** | Instruction tha "kavita ka images or video mai koi change nhi" — isliye chhoda. Bolne par kar denge |

> ⚠️ **Kavita ka text badalte waqt shabdon ki ginti nahi badalni.** Har verse ke saath `caption_cues_ms`
> hai — recording se naape gaye prati-shabd timings — aur highlight space par tod kar chalta hai. Ek
> shabd zyada hua to uske baad ka har cue galat shabd jalayega. Viram chinh apne shabd se juda rahe
> (`सजाया।`, `चले।”`). Abhi: T5 7/7, T6 8/8, T7 7/7.

## 3. Transition screens (deck p. 6, 7, 9)

| # | Review 2 ki line | Status |
|---|---|---|
| 3.1 | "ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें!" | ⬜ OPEN |
| 3.2 | "ये कविता सुनकर मुझे तो बहुत मज़ा आया, लेकिन मेले में भीड़ की वजह से सभी जोड़ियाँ बिछड़ गईं। आइए साथ मिलकर ढूँढ़ते हैं। चलिए, साथ में करें!" | ⬜ OPEN — abhi `vo_bridge_lost` chal raha hai |
| 3.3 | "वाह! अब आपकी बारी।" | ⬜ OPEN |

Swiftee ki transition animation khud ✅ ho chuki hai (`sw_peek_hd.webp`, teenon gates par) — sirf
ye teen lines record honi hain.

## 4. Guided questions (deck p. 7)

| # | Review 2 kehta hai | Status | Note |
|---|---|---|---|
| 4.1 | Galat attempt par **red outline nahi, wiggle** | ✅ DONE | Teenon feedback systems se red hata — card, option, gate |
| 4.2 | Heading → **सही जोड़ी चुनिए।** | ✅ DONE | G1–G4 |
| 4.3 | **घोड़ा:** image upar word ke saath; options sirf words | ✅ DONE | G4 — ghoda 300px stimulus mein, teen word buttons |
| 4.4 | शेरनी hint ladder (3 rungs) | 🎙️ VO PENDING | G1 mein 2 hi distinct clips — **`vo_h3_sherni` chahiye** |
| 4.5 | मोर hint ladder (3 rungs) | 🎙️ VO PENDING | G2 — **`vo_h3_mor` chahiye** |
| 4.6 | बकरी hint ladder (3 rungs) + VO "बकरी मेले में किसके साथ आई थी?" | 🎙️ VO PENDING | G3 — **`vo_h3_bakri` chahiye** |
| 4.7 | घोड़ा hint ladder (3 rungs) | 🎙️ VO PENDING | G4 — ladder authored, **`vo_h3_ghoda` chahiye** |

## 5. Practice — वाक्य पूरा कीजिए (deck p. 8–9)

| # | Review 2 kehta hai | Status | Note |
|---|---|---|---|
| 5.1 | **Delete slide** ×2 | ✅ DONE | G5 (जाता है/जाती है bins) aur P1 (बैल wali जोड़ी) hate |
| 5.2 | **Delete slide P3** | ✅ DONE | Purana P3 hata (G6 wahi mechanic hai aur rehta hai) |
| 5.3 | बकरा घास hint ladder (3 rungs) | 🎙️ VO PENDING | P2 ke chaaron rung ek hi clip par hain — **`vo_h2_sentence`, `vo_h3_sentence` chahiye** |
| 5.4 | Naya slide: **शेरनी मेले में ……** (जाता है / जाती है) + image | ✅ DONE (screen) | P3 — `pic_sherni_mela` laga hai |
| 5.5 | Naya slide: **बंदर पेड़ पर ……** (चढ़ता है / चढ़ती है) + image | ✅ DONE (screen) | P4 — `pic_bandar_ped` laga hai |
| 5.6 | Dono ke hint ladders | 🎙️ VO PENDING | Neeche full list |

## 6. झूला game (deck p. 9–10)

| # | Review 2 kehta hai | Status |
|---|---|---|
| 6.1 | Purana game delete, naya झूला game | ✅ DONE — `WHEEL_PAIRS`, P5, full screen |
| 6.2 | Q1 मोरनी · मोर / मुर्गी / घोड़ा · सahi **मोर** | ✅ DONE |
| 6.3 | Q2 बकरा · बिल्ली / बकरी / भेड़ · sahi **बकरी** | ✅ DONE |
| 6.4 | Q3 हाथी · हथिनी / घोड़ी / शेरनी · sahi **हथिनी** | ✅ DONE |
| 6.5 | Q4 चुहिया · चूहा / खरगोश / गाय · sahi **चूहा** | ✅ DONE |
| 6.6 | Q5 घोड़ा · हथिनी / घोड़ी / घोड़नी · sahi **घोड़ी** | ✅ DONE |
| 6.7 | Q6 मुर्गी · मुर्गा / मोर / तोता · sahi **मुर्गा** | ✅ DONE |
| 6.8 | चित्र में जानवर झूले पर बैठा dikhe | ✅ DONE — jaanwar seat par baithe hain, nichla hissa cushion ke aage wale hisse ke peeche |
| 6.9 | Galat par wiggle, sahi par जोड़ी झूले par baithe, झूला aage badhe, agla prashn | ✅ DONE |
| 6.10 | Sab जोड़ियाँ baithne par झूला chal pade aur game khatam | ✅ DONE — poora ek chakkar, phir slide complete |
| 6.11 | Chhe prashnon ki VO | 🎙️ VO PENDING — neeche list |

---

## 🎙️ Recording list — jo abhi chahiye

Saari ids card mein authored hain; sirf files nahi hain. File `assets/VO/<id>.ogg`.

**Guided hint 3 (4 clips)**

| id | line |
|---|---|
| `vo_h3_sherni` | यह शेर है, यह सही उत्तर है, इसपर टैप कीजिए। |
| `vo_h3_mor` | यह मोरनी है, यह सही उत्तर है, इसपर टैप कीजिए। |
| `vo_h3_bakri` | यह बकरा है, यह सही उत्तर है, इसपर टैप कीजिए। |
| `vo_h3_ghoda` | यह घोड़ी शब्द है, यह सही उत्तर है, इसपर टैप कीजिए। |

**बकरा घास — P2 (2 clips)**

| id | line |
|---|---|
| `vo_h2_sentence` | हम वाक्य में बोलते हैं, बकरा घास खा रहा है। |
| `vo_h3_sentence` | रहा है पर टैप कीजिए और वाक्य पूरा कीजिए। |

**शेरनी वाक्य — P3 (5 clips)**

| id | line |
|---|---|
| `vo_q_sentence_sherni` | वाक्य पूरा कीजिए। |
| `vo_h1_sentence_sherni` | सोचिए, वाक्य में जाता है आएगा या जाती है आएगा? |
| `vo_h2_sentence_sherni` | हम वाक्य में बोलते हैं, शेरनी मेले में जाती है। |
| `vo_h3_sentence_sherni` | जाती है पर टैप कीजिए और वाक्य पूरा कीजिए। |
| `vo_c_sentence_sherni` | (correct par shabaashi) |

**बंदर वाक्य — P4 (5 clips)**

| id | line |
|---|---|
| `vo_q_sentence_bandar` | वाक्य पूरा कीजिए। |
| `vo_h1_sentence_bandar` | सोचिए, वाक्य में चढ़ता है आएगा या चढ़ती है आएगा? |
| `vo_h2_sentence_bandar` | हम वाक्य में बोलते हैं, बंदर पेड़ पर चढ़ता है। |
| `vo_h3_sentence_bandar` | चढ़ता है पर टैप कीजिए और वाक्य पूरा कीजिए। |
| `vo_c_sentence_bandar` | (correct par shabaashi) |

**झूला game — P5 (7 clips)**

| id | line |
|---|---|
| `vo_wheel_intro` | (game ka intro, optional) |
| `vo_wq_morni` | मोरनी की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |
| `vo_wq_bakra` | बकरे की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |
| `vo_wq_hathi` | हाथी की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |
| `vo_wq_chuhiya` | चुहिया की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |
| `vo_wq_ghoda` | घोड़े की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |
| `vo_wq_murgi` | मुर्गी की जोड़ी को चुनिए और उसके साथ झूले पर बैठाइए। |

**Transition screens (3 clips)** — sections 3.1 / 3.2 / 3.3 ki lines.

Kul **26 clips**. Inke bina screen chalti hai, bas chup rehti hai.

---

## ⬜ Decisions needed

1. **Title** — "जोड़ी मिलाइए" karna hai? Tab `title.png` bhi naya chahiye.
2. **mor-morni ka size** — Review 2 bada bolta hai, baad ka instruction chhota. Kaunsa final?
3. **Change image of murgi** — kavita ki image hai; "kavita mein koi change nahi" wale instruction ke chalte roka hua hai.

## ✅ Jo Review 2 ke bahar bhi theek hua

Ye deck mein nahi likha tha par isi round mein aaya, taaki record rahe:

- झूला ki poori geometry supplied reference se naapi gayi — buckets spokes ke node par, wheel apni dhuri par ghoomta hai (pehle dhuri se 25px neeche ke bindu par ghoom raha tha)
- Background SVG ke apne crop se dobara banaya, blur hata (`filter0_f` = stdDeviation 0)
- हाथी / हथिनी / चूहा / चुहिया ki nayi images — checkerboard background hata kar
- झूला ka opening: chhe buckets, phir ghoomna, phir baaki blur, phir shabd
- जोड़ी mein dono jaanwar ek doosre ki taraf dekhte hain
