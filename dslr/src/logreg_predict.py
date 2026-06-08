import pandas as pd
import json
import os

from utils.load_csv import load_csv
from utils.math_utils import calculate_sigmoid


def write_predictions(predictions: list[str]) -> None:
    """Writes predicted houses to houses.csv."""
    file_path = "houses.csv"
    file_dir = os.path.dirname(file_path)
    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)

    houses_df = pd.DataFrame({
        "Index": range(len(predictions)),
        "Hogwarts House": predictions
    })
    houses_df.to_csv(file_path, index=False)


def normalize_from_stats(
    features: pd.DataFrame, norm_stats: dict
) -> pd.DataFrame:
    """Normalizes test features using training normalization statistics."""
    norm_features = pd.DataFrame()
    for feature in features.columns:
        mean = norm_stats[feature]["mean"]
        std = norm_stats[feature]["std"]
        filled_feature = features[feature].fillna(mean)
        norm_features[feature] = (filled_feature - mean) / std
    return norm_features


def calculate_probabilities(
    features: pd.DataFrame, model_data: dict
) -> list[str]:
    """Predicts the most likely Hogwarts house for each student."""
    predictions = []
    for student_index in range(len(features)):
        best_house = None
        best_probability = -1
        for house in model_data["models"]:
            weights = model_data["models"][house]["weights"]
            bias = model_data["models"][house]["bias"]
            score = bias
            for index in range(len(features.columns)):
                score += (weights[index] * features.iloc[student_index, index])
            probability = calculate_sigmoid(score)
            if probability > best_probability:
                best_probability = probability
                best_house = house
        predictions.append(best_house)
    return predictions


def main() -> None:
    dataset_path = "./data/dataset_test.csv"
    if not os.path.exists(dataset_path):
        print(f"ERROR : file {dataset_path} does not exist.")
        return
    _, features = load_csv(dataset_path, False)
    if features is None:
        return

    file_path = "models/model.json"
    if not os.path.exists(file_path):
        print(f"ERROR : file {file_path} does not exist.")
        return

    with open(file_path, "r") as file:
        model_data = json.load(file)
    selected_features = model_data["features"]
    norm_stats = model_data["normalization"]
    features = features[selected_features]
    features = normalize_from_stats(features, norm_stats)
    predictions = calculate_probabilities(features, model_data)
    write_predictions(predictions)


if __name__ == "__main__":
    main()
