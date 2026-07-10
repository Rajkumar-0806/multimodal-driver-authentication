# Configuration Guide

This document summarizes the software configuration, training parameters, optimization settings, and implementation details used in the proposed **Reliability-Aware Adaptive Multimodal Fusion Framework for Continuous Driver Authentication Under Non-Stationary Sensing**.

---

# Software Environment

The experiments were conducted using the following software environment.

| Component | Version |
|-----------|---------|
| Python | 3.10+ |
| PyTorch | 2.x |
| NumPy | Latest stable |
| OpenCV | Latest stable |
| Scikit-learn | Latest stable |
| Matplotlib | Latest stable |
| Pandas | Latest stable |

GPU acceleration is recommended for training.

---

# Hardware Configuration

The framework was evaluated on the following hardware configuration.

| Component | Specification |
|-----------|---------------|
| CPU | Intel Core i7 / AMD Ryzen 7 or equivalent |
| GPU | NVIDIA CUDA-enabled GPU |
| RAM | ≥16 GB |
| Storage | ≥20 GB |

---

# Training Configuration

The default training configuration is summarized below.

| Parameter | Value |
|-----------|------:|
| Batch Size | 64 |
| Epochs | 100 |
| Learning Rate | 0.0001 |
| Optimizer | Adam |
| Weight Decay | 1×10⁻⁵ |
| Random Seed | 42 |

---

# Reliability Estimation

Historical modality reliability is updated recursively.

| Parameter | Value |
|-----------|------:|
| Forgetting Factor (λ) | 0.90 |
| Reliability Initialization | 0.50 |

---

# Confidence Estimation

Confidence scores are computed independently for each modality.

| Modality | Confidence Estimator |
|----------|----------------------|
| Face | Image Quality Assessment + Liveness Detection |
| Voice | ASV Confidence + Signal-to-Noise Ratio |
| Gait | Motion Stability + Skeleton Consistency |

The confidence scores are normalized to the interval **[0,1]** before trust computation.

---

# Adaptive Threshold

Adaptive modality selection employs the following parameters.

| Parameter | Value |
|-----------|------:|
| Nominal Threshold (δ₀) | 0.60 |
| Adaptation Coefficient (κ) | 0.25 |

The threshold is computed globally for all modalities during each authentication cycle.

---

# Trust Computation

The trust score integrates

- Historical Reliability
- Instantaneous Confidence

to determine the contribution of each modality during adaptive fusion.

---

# Dataset Configuration

| Dataset | Split |
|----------|-------|
| Training | 70% |
| Validation | 10% |
| Testing | 20% |

Identity-disjoint partitions are maintained throughout all experiments.

---

# Evaluation Metrics

The following evaluation metrics are computed.

- Authentication Accuracy
- Precision
- Recall
- F1-score
- Equal Error Rate (EER)
- ROC Curve
- Area Under the ROC Curve (AUC)

---

# Robustness Evaluation

The proposed framework is evaluated under

- Illumination variation
- Acoustic noise
- Missing modalities
- Sensor degradation
- Distribution shift

Additional experiments investigate

- One available modality
- Two available modalities
- Three available modalities

under

- Mild
- Moderate
- Severe degradation

---

# Randomness Control

To improve reproducibility,

- Random seeds are fixed whenever possible.
- Subject partitions remain unchanged.
- Hyperparameters are identical across all experiments.
- Evaluation metrics are computed using the same protocol.

---

# Expected Results

Representative performance reported in the manuscript.

| Metric | Value |
|--------|------:|
| Authentication Accuracy | 98.60% |
| Equal Error Rate | 1.60% |
| Area Under ROC Curve | 0.991 |

Minor numerical variations may occur because of hardware differences and stochastic optimization.

---

# Configuration Files

The repository may include the following configuration files.

```
configs/

default.yaml

train.yaml

evaluation.yaml
```

Users are encouraged to modify configuration parameters only after reproducing the baseline experiments.

---

# Reproducibility Recommendation

For direct comparison with the published results, use

- identical dataset partitions,
- identical preprocessing procedures,
- identical optimization settings,
- identical evaluation metrics,
- identical random seed whenever possible.

This ensures consistent and reproducible experimental evaluation.
