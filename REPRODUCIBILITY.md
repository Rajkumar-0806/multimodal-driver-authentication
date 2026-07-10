# Reproducibility Guide

This document describes the procedures required to reproduce the experimental results reported in the manuscript:

> **Reliability-Aware Adaptive Multimodal Fusion for Robust Continuous Authentication Under Non-Stationary Sensing**

The objective of this repository is to ensure transparent and reproducible evaluation of the proposed reliability-aware multimodal authentication framework.

---

# Reproducibility Checklist

| Item | Status |
|------|:------:|
| Source code | ✓ |
| Model implementation | ✓ |
| Training pipeline | ✓ |
| Evaluation pipeline | ✓ |
| Dataset preparation guide | ✓ |
| Hyperparameter configuration | ✓ |
| Experimental protocol | ✓ |
| Performance metrics | ✓ |
| Dataset split documentation | ✓ |
| Reproducibility instructions | ✓ |

---

# Experimental Environment

The experiments were conducted using the following software environment.

| Component | Specification |
|-----------|---------------|
| Python | 3.10 or later |
| Deep Learning Framework | PyTorch 2.x |
| Operating System | Windows / Ubuntu Linux |
| GPU | NVIDIA CUDA-enabled GPU (recommended) |

The implementation is compatible with CPU execution, although GPU acceleration is recommended for training.

---

# Datasets

The proposed framework uses three publicly available benchmark datasets.

| Dataset | Modality |
|----------|----------|
| CASIA-B | Gait |
| VoxCeleb | Voice |
| LFW | Face |

The datasets are **not redistributed** because of their respective licensing agreements.

Please obtain the datasets from their official websites.

Detailed preparation instructions are provided in **DATASETS.md**.

---

# Dataset Partitions

To eliminate identity leakage, all datasets employ **subject-disjoint partitions**.

| Partition | Percentage |
|-----------|-----------:|
| Training | 70% |
| Validation | 10% |
| Testing | 20% |

Each identity appears in only one partition.

No overlap exists between the training and testing identities.

---

# Temporal Synchronization

The proposed multimodal framework performs authentication using synchronized biometric observations.

Face images, voice recordings, and gait sequences belonging to the same authentication session are grouped prior to feature extraction.

Samples exhibiting

- missing modalities,
- inconsistent timestamps,
- corrupted observations,

are removed before training.

---

# Preprocessing

Each biometric modality undergoes an independent preprocessing stage.

## Face

- Face detection
- Face alignment
- Image normalization
- Image resizing

---

## Voice

- Audio resampling
- Signal normalization
- Silence removal
- Noise suppression

---

## Gait

- Sequence normalization
- Motion normalization
- Temporal alignment
- Skeleton consistency verification

---

# Model Training

Training is initiated using

```bash
python train.py
```

The training pipeline automatically performs

- data loading,
- feature extraction,
- reliability estimation,
- confidence estimation,
- trust-aware adaptive fusion,
- model optimization.

---

# Evaluation

Evaluation is performed after model training.

The following performance metrics are reported.

- Authentication Accuracy
- Equal Error Rate (EER)
- Precision
- Recall
- F1-score
- ROC Curve
- Area Under the Curve (AUC)

---

# Hyperparameters

The experiments employ a fixed hyperparameter configuration throughout all datasets.

Representative parameters include

| Hyperparameter | Value |
|----------------|------:|
| Optimizer | Adam |
| Learning Rate | 0.0001 |
| Batch Size | 64 |
| Epochs | 100 |
| Random Seed | 42 |

The same configuration is maintained unless otherwise specified.

---

# Randomness Control

To improve reproducibility,

- random seeds are fixed,
- deterministic operations are preferred whenever supported by the deep learning framework,
- dataset partitions remain unchanged throughout all experiments.

---

# Experimental Protocol

The following protocol is adopted for all experiments.

1. Download the datasets.
2. Organize the datasets according to **DATASETS.md**.
3. Install all dependencies.
4. Train the proposed framework.
5. Evaluate the trained model.
6. Compare the obtained metrics with those reported in the manuscript.

---

# Expected Results

The proposed framework demonstrates robust continuous authentication under changing sensing environments.

Representative performance reported in the manuscript includes

| Metric | Value |
|--------|------:|
| Authentication Accuracy | 98.60% |
| Equal Error Rate | 1.60% |
| Area Under ROC Curve | 0.991 |

Minor numerical variations may occur because of hardware differences and stochastic optimization.

---

# Repository Contents

The repository includes

- implementation of the proposed framework,
- training pipeline,
- evaluation utilities,
- dataset preparation guide,
- documentation,
- configuration files.

The original datasets are intentionally excluded.

---

# Pretrained Models

Pretrained model checkpoints may be distributed separately because of repository size limitations.

If checkpoints are unavailable, users can reproduce the reported experiments by following the training procedure described in this repository.

---

# Citation

If this repository contributes to your research, please cite the accompanying publication.

```bibtex
@article{rajkumar2026reliability,
title={Reliability-Aware Adaptive Multimodal Fusion for Robust Continuous Authentication Under Non-Stationary Sensing},
author={Rajkumar, S. C. and others},
journal={Pattern Analysis and Applications},
year={2026},
note={Under Review}
}
```

---

# Contact

For implementation-related questions, please open a GitHub Issue or contact the corresponding author.

---

# Disclaimer

This repository is intended for academic research and educational purposes.

The datasets remain the property of their respective providers and are subject to their individual licensing terms.
