# A principal component entropy metric for assessing global synchronicity in EEG signals

This repository contains the source code for the project of the course _Biomedical Signal Processing 2026/2027_ - _Università degli studi di Milano_.
The source code was based on some sections of the paper: "A principal component entropy metric for assessing global synchronicity in EEG signals" [https://doi.org/10.1038/s41598-026-36434-0].

## Contents
This repository contains two notebooks:
- `kuramoto.ipynb` which aims to reproduce the evaluation of PC-entropy on synthetic data produced by the Kuramoto model.
- `eeg-arithmetic-task.ipynb` which aims to reproduce the analysis on the Physionet dataset _EEG During Mental Arithmetic Tasks_ [https://physionet.org/content/eegmat/1.0.0/].

## Installation

Clone the repository on your machine:

```bash
git clone https://github.com/francodesource/principal-component-entropy.git
cd principal-component-entropy
```

Then create a virtual environment, activate it and install the dependencies listed in `requirements.txt`.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows

Using PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Once the environment is active, launch JupyterLab to open the notebooks:

```bash
jupyter lab
```

To leave the virtual environment, run `deactivate`.

## Usage

### Saving images
To toggle the image saving process locate the cell with this line of code:
```python
ims = ImageSaver(save_imgs=True)
```
and change the parameter `save_imgs` as desired.

### Dataset
The notebook will automatically download the dataset from PhysioNet.
