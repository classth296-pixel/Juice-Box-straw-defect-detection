
# Juice Box Straw Defect Detector

A Streamlit-based web application that uses a YOLO image classification model to identify defects in juice box straws.

## Overview

This application allows users to upload an image of a juice box straw and automatically classifies it into one of the predefined defect categories using a trained YOLO model.

## Features

* Upload JPG, JPEG, or PNG images
* Fast YOLO-based image classification
* Displays predicted defect category
* Shows prediction confidence score
* Simple and user-friendly interface

## Defect Categories

The model can classify images into the following categories:

* Bent
* Good
* Loose
* Missing
* Pierced

## Usage

1. Upload an image using the file uploader.
2. Wait for the model to process the image.
3. View the predicted defect class and confidence score.
4. The uploaded image will be displayed for reference.

## Technology Stack

* Streamlit
* Ultralytics YOLO
* OpenCV
* NumPy
* Pillow
* PyTorch

## Model

The application uses a custom-trained YOLO classification model (`best.pt`) for defect detection.

## Author

Manoj Kumar
