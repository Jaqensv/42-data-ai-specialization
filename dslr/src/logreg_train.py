import pandas as pd
import json
import time
import os

from utils.load_csv import load_csv
from utils.normalization import normalize_stats
from utils.math_utils import calculate_sigmoid


def display_training() -> None:
    """Displays a short training animation in the terminal."""
    states = [
        "Training   ",
        "Training . ",
        "Training ..",
        "Training ..."
    ]
    for state in states:
        print(state, end="\r")
        time.sleep(0.3)


def write_model(models: dict, features: list, norm_stats: dict) -> None:
    """Writes trained models and preprocessing data to a JSON file."""
    if not models:
        print("No trained models to write.")
        return

    file_path = "models/model.json"
    file_dir = os.path.dirname(file_path)
    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)

    model_data = {
        "features": features,
        "normalization": norm_stats,
        "models": models
    }
    with open(file_path, "w+") as file:
        json.dump(model_data, file, indent=4)


def train_binary_model(
    features: pd.DataFrame, house_binary: list
) -> tuple[list[float], float]:
    """Trains a binary logistic regression model for one Hogwarts house."""
    if features.empty:
        raise ValueError("Features dataframe is empty.")
    if len(features) != len(house_binary):
        raise ValueError("Features and binary labels lengths do not match.")
    weights = [0] * len(features.columns)
    bias = 0
    learning_rate = 0.5
    features_array = features.to_numpy()
    for epoch in range(1000):
        gradient_weight = [0] * len(features.columns)
        gradient_bias = 0
        for student_index in range(len(features_array)):
            score = bias
            for index in range(len(features.columns)):
                score += weights[index] * features_array[student_index][index]
            prediction = calculate_sigmoid(score)
            error = prediction - house_binary[student_index]
            gradient_bias += error
            for index in range(len(features.columns)):
                gradient_weight[index] += (
                    error * features_array[student_index][index]
                )
        for index in range(len(features.columns)):
            gradient_weight[index] /= len(features)
            weights[index] -= learning_rate * gradient_weight[index]
        gradient_bias /= len(features)
        bias -= learning_rate * gradient_bias
    return weights, bias


def train_model(
    features: pd.DataFrame, labels: dict, norm_stats: dict
) -> None:
    """Trains one binary model per house and writes them to a JSON file."""
    if not labels:
        print("No binary labels available.")
        return
    models = {}
    for house in labels:
        display_training()
        weights, bias = train_binary_model(features, labels[house])
        models[house] = {
            "weights": weights,
            "bias": bias
        }
    write_model(models, list(features.columns), norm_stats)


def create_labels(houses: pd.Series) -> dict:
    """Creates one-vs-all binary labels for each Hogwarts house."""
    if houses is None or houses.empty:
        print("Houses series is empty.")
        return {}
    houses_index = (
        "Gryffindor",
        "Hufflepuff",
        "Ravenclaw",
        "Slytherin"
    )
    labels = {
        "Gryffindor": [],
        "Hufflepuff": [],
        "Ravenclaw": [],
        "Slytherin": []
    }
    for house in houses:
        for index in houses_index:
            labels[index].append(int(house == index))
    return labels


def normalize_from_stats(
    features: pd.DataFrame, norm_stats: dict
) -> pd.DataFrame:
    norm_features = pd.DataFrame()
    for feature in features.columns:
        mean = norm_stats[feature]["mean"]
        std = norm_stats[feature]["std"]
        filled_feature = features[feature].fillna(mean)
        norm_features[feature] = (filled_feature - mean) / std
    return norm_features


def main() -> None:
    """Loads training data, trains the models, and saves them to JSON."""
    dataset_path = "./data/dataset_train.csv"
    if not os.path.exists(dataset_path):
        print(f"ERROR : file {dataset_path} does not exist.")
        return
    houses, features = load_csv(dataset_path, True)
    if houses is None or features is None:
        return
    selected_features = ["Charms", "Transfiguration", "Astronomy"]
    if not all(feature in features.columns for feature in selected_features):
        print("One or more selected features are missing.")
        return
    features = features[selected_features]
    features, norm_stats = normalize_stats(features)
    labels = create_labels(houses)
    if not labels:
        return
    train_model(features, labels, norm_stats)


if __name__ == "__main__":
    main()
