# Experimental Protocol

This document provides the complete experimental protocol used to evaluate the proposed **Reliability-Aware Adaptive Multimodal Fusion Framework for Continuous Driver Authentication Under Non-Stationary Sensing**.

The protocol is intended to enable independent researchers to reproduce the experimental results reported in the accompanying manuscript.

---

# Experimental Workflow

The complete experimental pipeline consists of six sequential stages.

```
Dataset Preparation
        ↓
Data Preprocessing
        ↓
Feature Extraction
        ↓
Reliability-Aware Adaptive Fusion
        ↓
Model Training
        ↓
Performance Evaluation
```

---

# Step 1: Dataset Preparation

Download the following datasets from their official repositories.

| Dataset | Modality |
|----------|----------|
| CASIA-B | Gait |
| VoxCeleb | Voice |
| LFW | Face |

Organize the datasets according to the directory structure described in **DATASETS.md**.

---

# Step 2: Subject Partitioning

Identity-disjoint partitions are used for every dataset.

| Dataset Split | Percentage |
|---------------|-----------:|
| Training | 70% |
| Validation | 10% |
| Testing | 20% |

No subject appears in multiple partitions.

---

# Step 3: Multimodal Synchronization

Biometric observations belonging to the same authentication session are grouped prior to feature extraction.

Synchronization is performed using

- session identifiers,
- acquisition timestamps,
- subject identity.

Samples with

- missing modalities,
- corrupted files,
- inconsistent timestamps,

are discarded.

---

# Step 4: Preprocessing

## Face

- Face Detection
- Face Alignment
- Image Resizing
- Image Normalization

---

## Voice

- Audio Resampling
- Silence Removal
- Signal Normalization
- Noise Suppression

---

## Gait

- Sequence Normalization
- Skeleton Verification
- Motion Normalization
- Temporal Alignment

---

# Step 5: Feature Extraction

Each modality is processed independently.

Face

↓

Feature Vector

Voice

↓

Feature Vector

Gait

↓

Feature Vector

The extracted feature representations are subsequently provided to the adaptive fusion module.

---

# Step 6: Reliability Estimation

Historical reliability is recursively estimated using exponentially weighted observations.

The reliability score continuously adapts according to the long-term behavior of each biometric modality.

---

# Step 7: Confidence Estimation

Modality-specific confidence is computed independently.

| Modality | Confidence Indicators |
|----------|-----------------------|
| Face | Image Quality + Liveness Detection |
| Voice | ASV Confidence + Signal-to-Noise Ratio |
| Gait | Motion Stability + Skeleton Consistency |

---

# Step 8: Trust Computation

Historical reliability and instantaneous confidence are combined to compute the trust score.

The trust score determines the contribution of each modality during multimodal fusion.

---

# Step 9: Adaptive Modality Selection

Modalities with trust scores below the adaptive threshold are temporarily excluded from the fusion process.

The adaptive threshold is computed using

\[
\delta_t=\delta_0+\kappa \cdot Var(T_t)
\]

where

- δ₀ = nominal threshold
- κ = adaptation coefficient

---

# Step 10: Trust-Aware Adaptive Fusion

The remaining modalities are fused according to their trust scores.

The proposed adaptive fusion suppresses degraded modalities while emphasizing reliable biometric evidence.

---

# Step 11: Continuous Authentication

Authentication decisions are continuously updated throughout the driving session.

The recursive trust update enables adaptation without retraining.

---

# Model Training

Training is performed using

```bash
python train.py
```

The optimization procedure includes

- forward propagation,
- reliability estimation,
- adaptive fusion,
- backpropagation,
- parameter update.

---

# Evaluation Metrics

The following performance metrics are reported.

| Metric |
|---------|
| Accuracy |
| Precision |
| Recall |
| F1-score |
| Equal Error Rate (EER) |
| Area Under ROC Curve (AUC) |

---

# Robustness Evaluation

The proposed framework is evaluated under

- illumination variation,
- acoustic noise,
- missing modalities,
- distribution shift,
- sensor degradation.

Additional experiments investigate

- one available modality,
- two available modalities,
- three available modalities,

under

- mild,
- moderate,
- severe degradation.

---

# Ablation Study

The contribution of each framework component is evaluated by removing

- reliability estimation,
- confidence estimation,
- adaptive modality selection,
- trust-aware fusion.

Performance differences are analyzed using the reported evaluation metrics.

---

# Statistical Analysis

Where applicable, multiple experimental runs should be performed using different random initialization seeds.

Reported results correspond to the mean performance across repeated experiments.

---

# Expected Performance

Representative results reported in the manuscript.

| Metric | Value |
|--------|------:|
| Authentication Accuracy | 98.60% |
| Equal Error Rate | 1.60% |
| Area Under ROC Curve | 0.991 |

---

# Hardware Recommendation

Recommended hardware configuration.

| Component | Recommendation |
|-----------|----------------|
| CPU | Intel Core i7 / AMD Ryzen 7 or higher |
| GPU | NVIDIA RTX series |
| Memory | ≥16 GB RAM |
| Storage | ≥20 GB |

---

# Reproducibility

Following this protocol should reproduce the experimental methodology presented in the accompanying manuscript, provided identical dataset partitions, preprocessing procedures, and hyperparameter settings are employed.
