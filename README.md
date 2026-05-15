# XAI Chest X-ray Diagnosis Dissertation Project

This repository contains the code for my dissertation project, which investigates explainable AI Chest X-rays Disease Classification using Deep Learning and Explainable AI for Medical Diagnostic Support.

## Project Aim

The aim of this project is to develop and evaluate a DenseNet121 model using XAI techniques with Grad-CAM for a multi-class Disease classifcation approach for chest X-ray images.
## Models

- DenseNet121: main model
- ResNet50: benchmark model

## Training Approach

The models use pretrained weights and are fine-tuned on the folowing datasets.
http://db.jsrt.or.jp/eng.php
https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset
https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database
https://www.kaggle.com/datasets/nih-chest-xrays/data

## Explainability
The model will be evaluated on a various of quantative metrics such as Accuracy, Precision, F1-score and Confusion matrix etc.
Grad-CAM will be used to visualise which areas of the chest X-ray contribute most to the model's predictions.

## Repository Structure

- `notebooks/`: Colab notebooks used for setup, training, evaluation, and XAI.
- `src/`: Python scripts for reusable code.
- `reports/`: Project notes and dissertation-related documentation.

## Data

Datasets are not stored in this repository because medical imaging datasets are large. The datasets are stored separately in Google Drive.
