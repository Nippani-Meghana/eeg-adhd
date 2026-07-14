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

## Template — copy this block for each paper

### Paper N: [title]

**Citation:**
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

## Starter prompts per tier (my own analysis — verify against each paper, don't just accept)

These are questions to interrogate each paper with. I fill in the answers myself.

### Tier 1 — Classical ML (ADHD-AID)
- Do the hand-crafted features (band-power, entropy, nonlinear, statistical) assume stationarity within a segment? Is EEG actually stationary over that window?
- Does the classifier treat each segment as an independent sample? **If segments from one child appear in both train and test, is the model learning "ADHD" or learning "this child"?** ← the central assumption to test
- Feature selection: is it run *inside* or *outside* the CV loop? If outside, that's selection leakage — a second, subtler inflation.

### Tier 2 — Deep Learning (CNN / spectrogram)
- The network learns its own features — but does the signal→image transform (STFT window, overlap) preserve the discriminative information, or throw it away before the CNN sees it?
- **121 subjects is small for DL.** Does the method assume enough data to avoid overfitting? Watch for: train accuracy ≫ val accuracy.
- How do 19 channels become a CNN input (stacked / averaged / one-image-per-channel)? This is usually under-specified and high-impact.
- Transfer learning from ImageNet: does a network pretrained on natural images transfer sensibly to spectrograms? What's the implicit assumption there?

### Tier 3 — Advanced (TBD with professor)
- If connectivity / graph-based: assumes relationships *between* channels carry signal that Tiers 1–2 ignored. Is that assumption supported by ADHD neuroscience (e.g. fronto-parietal differences)?
- Does added complexity actually beat the honest subject-wise baseline from Tiers 1–2, or only the inflated segment-wise numbers?
- **Sequencing note:** choose this paper *before* finalizing Paper 2, so Paper 2's output representation feeds naturally into it.

---

## Running log of cross-cutting lessons

_(The meta-observations that span papers — this section is the actual deliverable.)_

1. **Splitting strategy dominates reported accuracy** on this dataset. Segment-wise CV inflates; subject-wise/LOSO is honest. Categorize every paper in my review by which they used. (e.g. TMP19 reports 95.57% 10-fold vs. 77.93% LOSO — same paper, same data.)
2.
3.