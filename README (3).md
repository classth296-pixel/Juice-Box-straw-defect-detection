# Juice Box Straw Defect Detector

A computer vision system that detects manufacturing/packaging defects in juice box straw attachments using **YOLOv8** object detection. Built to identify quality control issues such as missing straws, misaligned straws, and torn wrapper seals from product images.

## Overview

In beverage packaging lines, straw attachment defects are a common quality control issue that's costly to catch manually at scale. This project trains a **YOLOv8 image classification** model to automatically assign a single defect label to each product image, enabling faster and more consistent QC checks compared to manual visual inspection.

## Defect Classes

The model is trained to detect the following categories:

| Class | Description |
|---|---|
| `Bent` | Straw is bent or crooked |
| `Good` | No defect detected (normal/passing unit) |
| `Loose` | Straw is attached but not securely fixed |
| `Missing` | Straw is absent from the packaging |
| `Pierced` | Straw has pierced through the box incorrectly (e.g. through the side instead of the marked entry point) |

## Dataset

- **Source:** Public dataset from Kaggle
- **Format:** Folder-per-class structure (standard for YOLOv8 classification)
- [**Structure:**](https://www.kaggle.com/datasets/jhamilgutierrez/juice-box-straw-defects)
  ```
  dataset/
  ├── train/
  │   ├── Bent/
  │   ├── Good/
  │   ├── Loose/
  │   ├── Missing/
  │   └── Pierced/
  ├── val/
  │   ├── Bent/
  │   ├── Good/
  │   ├── Loose/
  │   ├── Missing/
  │   └── Pierced/
  └── test/
      ├── Bent/
      ├── Good/
      ├── Loose/
      ├── Missing/
      └── Pierced/
  ```

> Note: Due to size/licensing, the dataset is not bundled in this repo. See [Dataset Setup](#dataset-setup) below for download instructions.

## Tech Stack

- **Model:** YOLOv8 (Ultralytics)
- **Language:** Python
- **Core libraries:** `ultralytics`, `opencv-python`, `numpy`, `matplotlib`
- **Environment:** Trained on Kaggle Notebooks (free GPU) / local CUDA setup

## Project Structure

```
juice-box-straw-defect-detector/
├── train.py                # Training script
├── predict.py               # Inference on new images
├── requirements.txt
├── notebooks/
│   └── training_notebook.ipynb
├── runs/                    # Training outputs (weights, logs, metrics)
└── README.md
```

## Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/juice-box-straw-defect-detector.git
cd juice-box-straw-defect-detector

# Install dependencies
pip install -r requirements.txt
```

## Dataset Setup

1. Download the dataset from Kaggle (link to be added once finalized).
2. Place it in the `dataset/` directory following the folder-per-class structure above, where each class (`Bent`, `Good`, `Loose`, `Missing`, `Pierced`) has its own subfolder under `train/`, `val/`, and `test/`.

## Training

```bash
yolo task=classify mode=train model=yolov8n-cls.pt data=dataset epochs=100 imgsz=224
```

Trained weights are saved under `runs/classify/train/weights/best.pt`.

## Inference

```bash
python predict.py --weights runs/classify/train/weights/best.pt --source path/to/image_or_folder
```

This outputs the predicted class label (`Bent`, `Good`, `Loose`, `Missing`, or `Pierced`) along with the model's confidence score for each image.

## Results

| Metric | Value |
|---|---|
| Top-1 Accuracy | TBD |
| Top-5 Accuracy | TBD |
| Precision (per class) | TBD |
| Recall (per class) | TBD |

*(Update this table once training/evaluation is complete.)*

## Future Improvements

- Add Grad-CAM visualizations to interpret which image regions drive each classification
- Deploy as a real-time inspection pipeline (webcam/conveyor feed)
- Export to ONNX/TensorRT for edge deployment
- Add a simple Streamlit dashboard for QC teams to review flagged units
- Address class imbalance if `Good` samples significantly outnumber defect classes

## License

This project is open-source under the MIT License.
