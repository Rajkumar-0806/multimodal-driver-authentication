# Installation Guide

This document describes the software environment required to reproduce the experiments presented in the manuscript:

> **Reliability-Aware Adaptive Multimodal Fusion for Robust Continuous Authentication Under Non-Stationary Sensing**

---

# System Requirements

The implementation has been developed and evaluated using the following environment.

| Component | Version |
|-----------|---------|
| Operating System | Windows 10/11 or Ubuntu 20.04+ |
| Python | 3.10 or later |
| PyTorch | 2.x |
| CUDA | 11.x or later (recommended) |
| GPU | NVIDIA GPU (recommended) |
| RAM | ≥16 GB |
| Storage | ≥20 GB available |

Although GPU acceleration is recommended for training, inference can also be performed on CPU.

---

# Clone Repository

Clone the repository

```bash
git clone https://github.com/Rajkumar-0806/multimodal-driver-authentication.git
```

Move into the project directory

```bash
cd multimodal-driver-authentication
```

---

# Create Python Environment

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

Alternatively, create the Conda environment.

```bash
conda env create -f environment.yml
```

Activate the environment.

```bash
conda activate multimodal-auth
```

---

# Verify Installation

Verify that PyTorch is correctly installed.

```bash
python -c "import torch; print(torch.__version__)"
```

Verify CUDA availability.

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

---

# Repository Structure

```
multimodal-driver-authentication/

│── train.py
│── models.py
│── dataset.py
│── utils.py

│── docs/

│── checkpoints/

│── Final/

│── requirements.txt

│── README.md
```

---

# Dataset Preparation

The implementation utilizes three publicly available datasets.

| Dataset | Modality |
|----------|----------|
| CASIA-B | Gait |
| VoxCeleb | Voice |
| LFW | Face |

The datasets are **not redistributed** through this repository because of their respective licensing agreements.

Detailed dataset preparation instructions are provided in **DATASETS.md**.

---

# Running the Framework

Training

```bash
python train.py
```

The training procedure performs

- Dataset loading
- Feature extraction
- Reliability estimation
- Trust-aware adaptive fusion
- Model optimization

---

# Model Checkpoints

Trained model weights should be placed inside

```
checkpoints/
```

If pretrained weights are released separately because of repository size limitations, download instructions will be provided inside

```
checkpoints/README.md
```

---

# Troubleshooting

### CUDA not detected

Verify

```bash
nvidia-smi
```

and ensure that the installed CUDA version is compatible with the installed PyTorch version.

---

### Module import error

Install missing packages

```bash
pip install -r requirements.txt
```

---

### Out-of-memory error

Reduce the batch size inside the training configuration.

---

# Reproducibility

To reproduce the results reported in the manuscript, please ensure that

- the same dataset partitions are used,
- identity-disjoint splits are maintained,
- preprocessing follows the procedure described in **DATASETS.md**,
- training hyperparameters are identical to those reported in the manuscript.

---

# Support

For questions regarding the implementation, please open a GitHub Issue or contact the corresponding author.
