Readme
# Reliability-Aware Adaptive Multimodal Fusion for Continuous Driver Authentication Under Non-Stationary Sensing

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Research-orange.svg)]()

</p>

---

## Overview

This repository contains the official implementation accompanying the manuscript

> **Reliability-Aware Adaptive Multimodal Fusion for Robust Continuous Authentication Under Non-Stationary Sensing**

submitted to **Pattern Analysis and Applications**.

The proposed framework introduces a reliability-aware adaptive multimodal fusion strategy that continuously estimates modality trust and dynamically adapts biometric fusion under changing sensing environments. Unlike conventional multimodal authentication systems that rely on static fusion, the proposed approach jointly models historical reliability, instantaneous confidence estimation, and trust-aware adaptive attention to improve robustness under sensor degradation, distribution shift, and missing modalities.

---

## Key Features

- Reliability-aware multimodal fusion
- Continuous driver authentication
- Dynamic trust estimation
- Historical reliability learning
- Confidence-aware adaptive attention
- Adaptive modality selection
- Closed-loop reliability update
- Robust operation under non-stationary sensing
- Graceful degradation under missing modalities

---

## Repository Structure

```
multimodal-driver-authentication/
│
├── train.py
├── models.py
├── dataset.py
├── utils.py
│
├── Final/
│      Sample figures used in the manuscript
│
├── docs/
│      INSTALL.md
│      DATASETS.md
│      MODEL.md
│      TRAINING.md
│      TESTING.md
│      RESULTS.md
│      REPRODUCIBILITY.md
│
├── checkpoints/
│
├── requirements.txt
├── environment.yml
└── README.md
```

---

## Methodology

The proposed framework consists of five major stages.

1. Multimodal biometric acquisition
2. Modality-specific feature extraction
3. Reliability estimation
4. Trust-aware adaptive fusion
5. Continuous authentication

The fusion process jointly incorporates

- historical reliability
- instantaneous confidence
- adaptive trust estimation
- dynamic modality selection

to improve robustness under continuously changing sensing conditions.

---

## Supported Modalities

| Modality | Description |
|-----------|-------------|
| Face | Visual biometric authentication |
| Voice | Speaker authentication |
| Gait | Behavioural biometric authentication |

---

## Datasets

Experiments were conducted using publicly available datasets.

| Dataset | Purpose |
|----------|---------|
| CASIA-B | Gait Recognition |
| VoxCeleb | Speaker Recognition |
| LFW | Face Recognition |

The datasets are **not redistributed** through this repository due to their respective licensing agreements.

Please obtain them from their official providers.

---

## Dataset Split

All experiments employ **subject-disjoint partitions** to prevent identity leakage.

| Split | Percentage |
|--------|-----------:|
| Training | 70% |
| Validation | 10% |
| Testing | 20% |

Identity overlap between training and testing is not permitted.

Multimodal samples are temporally synchronized using acquisition session information before feature extraction and multimodal fusion.

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Training

Training can be started using

```bash
python train.py
```

The implementation automatically performs

- data loading
- feature extraction
- multimodal fusion
- reliability estimation
- trust-aware learning
- model optimization

---

## Evaluation

Performance is evaluated using

- Accuracy
- Precision
- Recall
- F1-score
- Equal Error Rate (EER)
- Area Under ROC Curve (AUC)

---

## Experimental Results

The proposed framework demonstrates improved robustness under

- illumination variation
- acoustic noise
- missing modalities
- sensor degradation
- distribution shift

The manuscript reports

- 98.6% Authentication Accuracy
- 1.6% Equal Error Rate
- 0.991 AUC

---

## Reproducibility

This repository provides

- source code
- model implementation
- dataset preparation guidelines
- training procedure
- evaluation workflow

Dataset redistribution is not permitted because of licensing restrictions.

---

## Citation

If you use this repository in your research, please cite

```bibtex
@article{rajkumar2026reliability,
title={Reliability-Aware Adaptive Multimodal Fusion for Robust Continuous Authentication Under Non-Stationary Sensing},
author={Rajkumar, S.C. and others},
journal={Pattern Analysis and Applications},
year={2026},
note={Under Review}
}
```

---

## Contact

Rajkumar S.C.

Email:
rajkumar@autmdu.in

---

## License

This repository is released for academic research purposes.
