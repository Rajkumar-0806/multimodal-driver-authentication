# Experimental Results

This document summarizes the experimental results obtained using the proposed **Reliability-Aware Adaptive Multimodal Fusion Framework for Continuous Driver Authentication Under Non-Stationary Sensing**.

The results presented here correspond to those reported in the accompanying manuscript submitted to **Pattern Analysis and Applications**.

---

# Evaluation Protocol

All experiments follow the evaluation protocol described in **EXPERIMENT_PROTOCOL.md**.

The framework is evaluated under realistic non-stationary sensing environments including

- illumination variation
- acoustic noise
- missing modalities
- sensor degradation
- distribution shift

Identity-disjoint subject partitions are maintained throughout all experiments.

---

# Performance Metrics

The following evaluation metrics are reported.

| Metric | Description |
|----------|-------------|
| Accuracy | Overall authentication accuracy |
| Precision | Positive predictive value |
| Recall | Sensitivity |
| F1-score | Harmonic mean of Precision and Recall |
| Equal Error Rate (EER) | False Acceptance = False Rejection |
| ROC Curve | Receiver Operating Characteristic |
| AUC | Area Under the ROC Curve |

---

# Overall Authentication Performance

The proposed framework achieves the following representative performance.

| Metric | Performance |
|---------|------------:|
| Authentication Accuracy | **98.60 %** |
| Equal Error Rate (EER) | **1.60 %** |
| Area Under ROC Curve (AUC) | **0.991** |

These results demonstrate the effectiveness of reliability-aware adaptive multimodal fusion for continuous driver authentication.

---

# Robustness Evaluation

The framework is evaluated under multiple challenging operating conditions.

## Illumination Variation

Face authentication remains reliable under changing lighting conditions through confidence-aware reliability estimation.

---

## Acoustic Noise

Voice authentication performance is preserved through adaptive trust estimation under noisy environments.

---

## Missing Modalities

The proposed adaptive modality selection mechanism enables graceful degradation when one or more biometric modalities become unavailable.

---

## Distribution Shift

Historical reliability estimation enables adaptation to changing sensing environments while maintaining stable authentication performance.

---

# Failure Case Analysis

Performance was further analyzed under progressive modality degradation.

The evaluation considers

- three available modalities
- two available modalities
- one available modality

under

- mild degradation
- moderate degradation
- severe degradation

The results demonstrate that authentication performance decreases gradually rather than catastrophically as sensing quality deteriorates, confirming the graceful degradation capability of the proposed reliability-aware adaptive fusion framework.

---

# Ablation Study

The contribution of each component was evaluated by removing individual modules from the proposed framework.

The investigated components include

- Reliability Estimation
- Confidence Estimation
- Adaptive Modality Selection
- Trust-Aware Fusion

The complete framework consistently achieves the highest authentication accuracy and the lowest Equal Error Rate, demonstrating the complementary contribution of each component.

---

# Adaptive Threshold Analysis

The proposed adaptive threshold was compared with a conventional fixed threshold.

The adaptive strategy consistently improves robustness by dynamically adjusting modality participation according to the variance of modality trust scores.

---

# Reliability Update Analysis

Replacing binary reliability feedback with continuous reliability estimation improves the stability of modality trust estimation under changing sensing environments.

The proposed recursive reliability update provides smoother trust evolution while preserving rapid adaptation to sensor degradation.

---

# Confidence Estimation

Confidence estimation combines modality-specific quality indicators.

| Modality | Confidence Indicators |
|----------|-----------------------|
| Face | Image Quality Assessment + Liveness Detection |
| Voice | Signal-to-Noise Ratio + ASV Confidence |
| Gait | Motion Stability + Skeleton Consistency |

---

# Qualitative Analysis

The proposed reliability-aware fusion framework

- suppresses unreliable biometric modalities,
- emphasizes trustworthy observations,
- dynamically adapts to changing sensing conditions,
- maintains stable continuous authentication.

---

# Reproducibility

To reproduce the reported results

1. Download the datasets.
2. Prepare the datasets following **DATASETS.md**.
3. Install all dependencies.
4. Train the framework using

```bash
python train.py
```

5. Evaluate the trained model.

The reported metrics should be comparable to those presented in the accompanying manuscript.

---

# Repository Outputs

Typical outputs generated during training and evaluation include

```
results/

Accuracy.csv

ROC_Curve.png

Confusion_Matrix.png

Training_Loss.png

Validation_Accuracy.png

Reliability_Curve.png

Failure_Case_Analysis.png
```

---

# Notes

Minor numerical differences may occur due to

- random initialization,
- hardware configuration,
- software version,
- floating-point implementation.

These differences are expected and do not affect the overall conclusions of the study.

---

# Correspondence with the Manuscript

The tables and figures generated by this repository correspond directly to the experimental evaluation presented in the accompanying manuscript.

Readers are encouraged to consult the manuscript for detailed discussions of the proposed methodology, theoretical analysis, and comparative evaluation.
