# XAI Chest X-ray Diagnosis Dissertation Project

This repository contains the code for my dissertation project, which investigates explainable artificial intelligence for chest X-ray diagnosis.

## Project Aim

The aim of this project is to develop and evaluate a deep learning model for chest X-ray diagnosis using explainable AI techniques.

## Models

- DenseNet121: main model
- ResNet50: benchmark model

## Training Approach

The models use pretrained weights and are fine-tuned on multiple chest X-ray datasets.

## Explainability

Grad-CAM will be used to visualise which areas of the chest X-ray contribute most to the model's predictions.

## Repository Structure

- `notebooks/`: Colab notebooks used for setup, training, evaluation, and XAI.
- `src/`: Python scripts for reusable code.
- `reports/`: Project notes and dissertation-related documentation.

## Data

Datasets are not stored in this repository because medical imaging datasets are large and may have usage restrictions. The datasets are stored separately in Google Drive.
