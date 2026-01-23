# ft_linear_regression

Simple implementation of a linear regression model in Python.
Project developed in the context of 42 curriculum.

## Description

This project implements a basic linear regression using gradient descent.
It allows:
- training a model on a dataset
- predicting prices from mileage
- evaluating the model using Mean Absolute Error (MAE)

## Project structure
```text
ft_linear_regression/
├── data/
│   └── data.csv
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py

## Requirements

- Python 3.x
- No external dependencies

## Usage

- Train the model : python3 src/train.py
- Predict a value : python3 src/predict.py
- Evaluate the model : python3 src/evaluate.py
