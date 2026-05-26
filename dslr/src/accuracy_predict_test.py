import pandas as pd
import json

from utils.load_csv import load_csv
from logreg_predict import normalize_from_stats, calculate_probabilities


def calculate_accuracy(predictions: list[str], houses: pd.Series) -> float:
    """Calculates prediction accuracy against expected houses."""

    correct = 0

    for index in range(len(predictions)):
        if predictions[index] == houses[index]:
            correct += 1

    return correct / len(predictions)


def main() -> None:

    houses, features = load_csv("data/dataset_train.csv", True)

    if features is None:
        return

    with open("src/models/model.json", "r") as file:
        model_data = json.load(file)

    selected_features = model_data["features"]
    norm_stats = model_data["normalization"]

    features = features[selected_features]
    features = normalize_from_stats(features, norm_stats)

    predictions = calculate_probabilities(features, model_data)
    accuracy = calculate_accuracy(predictions, houses)
    print(f"Accuracy: {accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()
