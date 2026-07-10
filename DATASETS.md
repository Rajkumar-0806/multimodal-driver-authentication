# Dataset Preparation Guide

This document describes the datasets, preprocessing pipeline, subject partitioning strategy, and temporal synchronization procedure used in the proposed reliability-aware multimodal authentication framework.

---

# Supported Datasets

The proposed framework utilizes three publicly available benchmark datasets representing complementary biometric modalities.

| Dataset | Modality | Purpose |
|----------|----------|---------|
| CASIA-B | Gait | Behavioral biometric recognition |
| VoxCeleb | Voice | Speaker authentication |
| LFW (Labeled Faces in the Wild) | Face | Facial authentication |

The original datasets are **not redistributed** through this repository due to their respective licensing agreements. Please download each dataset from its official source.

---

# Official Dataset Sources

## CASIA-B

Institute of Automation, Chinese Academy of Sciences

https://www.cbsr.ia.ac.cn/english/Gait%20Databases.asp

---

## VoxCeleb

University of Oxford

https://www.robots.ox.ac.uk/~vgg/data/voxceleb/

---

## LFW

University of Massachusetts Amherst

http://vis-www.cs.umass.edu/lfw/

---

# Dataset Organization

After downloading, organize the datasets using the following directory structure.

```
datasets/

├── CASIA-B/

├── VoxCeleb/

└── LFW/
```

---

# Subject-Disjoint Dataset Split

To prevent identity leakage between training and testing, all experiments employ subject-disjoint partitions.

| Partition | Percentage |
|-----------|-----------:|
| Training | 70% |
| Validation | 10% |
| Testing | 20% |

No subject appears simultaneously in multiple partitions.

The same identity-disjoint protocol is maintained throughout all experiments.

---

# CASIA-B Split

Each subject is assigned exclusively to one partition.

The gait sequences associated with each subject remain entirely within the corresponding partition.

No walking sequences belonging to a test subject are used during training.

---

# VoxCeleb Split

Speaker identities are divided using the same subject-disjoint protocol.

Each speaker contributes recordings to only one partition.

Speaker overlap between training and testing is not permitted.

---

# LFW Split

Identity-disjoint facial image partitions are employed.

Each individual contributes images to only one subset.

Identity leakage between partitions is strictly avoided.

---

# Temporal Alignment

The proposed multimodal authentication framework performs authentication using synchronized biometric observations.

Face images, gait sequences, and voice recordings are associated according to the same authentication session before feature extraction.

Only synchronized multimodal samples are used during multimodal fusion.

Samples with missing timestamps or incomplete modality observations are discarded before training.

---

# Preprocessing Pipeline

The preprocessing stage consists of three independent modality-specific pipelines.

## Face

The face preprocessing pipeline performs

- Face detection
- Face alignment
- Image normalization
- Image resizing
- Pixel normalization

before feature extraction.

---

## Voice

The voice preprocessing stage performs

- Audio resampling
- Silence removal
- Signal normalization
- Noise reduction
- Feature normalization

prior to speaker representation learning.

---

## Gait

The gait preprocessing stage performs

- Sequence extraction
- Frame normalization
- Skeleton consistency verification
- Motion normalization
- Temporal alignment

before gait feature extraction.

---

# Data Quality Control

During preprocessing, corrupted samples are automatically removed.

Typical exclusion criteria include

- missing frames,
- corrupted audio,
- incomplete gait sequences,
- duplicated samples,
- inconsistent timestamps.

---

# Data Augmentation

To improve generalization, standard data augmentation strategies may be applied during training.

Examples include

### Face

- Random horizontal flipping
- Brightness variation
- Contrast adjustment

### Voice

- Additive background noise
- Volume perturbation
- Time shifting

### Gait

- Sequence jittering
- Temporal cropping
- Motion perturbation

Data augmentation is performed only during training.

---

# Reproducibility

To ensure reproducibility,

- identical subject partitions are maintained throughout all experiments,
- preprocessing is deterministic,
- identical random seeds are used whenever possible,
- identical evaluation metrics are adopted across all datasets.

---

# Licensing

CASIA-B, VoxCeleb, and LFW remain the intellectual property of their respective providers.

Users are responsible for complying with the corresponding dataset licenses before using the proposed framework.

---

# Citation

Please cite the original dataset publications when using the datasets in your research.
