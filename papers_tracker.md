# EEG-ADHD Replication: Method Assumptions Tracker

**Dataset:** Nasrabadi et al. (2020), "EEG data for ADHD/Control children", IEEE Dataport (DOI 10.21227/rzfh-zn36).
121 subjects (61 ADHD, 60 control) · 19 channels · 128 Hz · visual-attention counting task · variable recording length per subject.

**Purpose of this doc:** For each paper I replicate, record what the method *assumes*, where those assumptions can silently break, and what I actually observed. The value of the literature review is in *these* comparisons — not in any single accuracy number.

**Rule I'm holding myself to:** keep the train/test split identical across all three papers (subject-wise, ideally LOSO) so that method complexity is the only variable.

---

## Cross-paper comparison table (fill in as I go)

| | Paper 1 (Classical ML) | Paper 2 (Deep Learning) | Paper 3 (Advanced) |
|---|---|---|---|
| Citation | Attallah, ADHD-AID, Biomimetics 2024 | _TBD_ | _TBD_ |
| Core method | Multi-res features + classifier | | |
| Input representation | Hand-crafted feature vector | | |
| Reported accuracy (paper) | 0.991 (10-fold) | | |
| **Their split strategy** | _verify: segment-wise?_ | | |
| **My accuracy (subject-wise)** | _TBD_ | | |
| Gap (their vs. my split) | _TBD_ | | |
| Training time / compute | | | |
| Hardest detail to replicate | | | |

---


### Paper N: [ADHD-AID: Aiding Tool for Detecting Children’s Attention Deficit Hyperactivity Disorder via EEG-Based Multi-Resolution Analysis and Feature Selection]

**Citation:** Attallah, O. ADHD-AID: Aiding Tool for Detecting Children’s Attention Deficit Hyperactivity Disorder via EEG-Based Multi-Resolution Analysis and Feature Selection. Biomimetics 2024, 9, 188. https://doi.org/10.3390/biomimetics9030188 

**Method in one sentence:**

#### Explicit assumptions (what the method takes as given)
- Input representation assumes: 
- Data assumes: 
- Model assumes: 
- Evaluation assumes:

#### Where it can silently break (failure modes)
- 

#### Under-specified in the paper (details I had to guess)
- 

#### What I observed
- Accuracy (their split): __ · Accuracy (subject-wise/LOSO): __
- Surprise / lesson:

---


### Tier 1 — Classical ML (ADHD-AID)


### Tier 2 — Deep Learning (CNN)


### Tier 3 — Advanced


---

## Running log of cross-cutting lessons



