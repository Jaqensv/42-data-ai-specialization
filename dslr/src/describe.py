from utils.math_utils import calculate_stats
from utils.load_csv import load_csv
import pandas as pd


def create_stats_dataframe(df: pd.DataFrame) -> pd.DataFrame | None:

    if df.empty:
        print("Stats dataframe is empty.")
        return None

    stats_dict = {}

    for column in df.columns:
        mean, quartile, std, min_value, max_value = calculate_stats(df[column])

        if quartile is None:
            continue

        stats_dict[column] = {}
        stats_dict[column]["Count"] = len(df[column])
        stats_dict[column]["Mean"] = mean
        stats_dict[column]["Std"] = std
        stats_dict[column]["Min"] = min_value
        stats_dict[column]["25%"] = quartile[0]
        stats_dict[column]["50%"] = quartile[1]
        stats_dict[column]["75%"] = quartile[2]
        stats_dict[column]["Max"] = max_value

    stats = pd.DataFrame(stats_dict)

    return stats


def main() -> None:

    y, X = load_csv("data/dataset_train.csv", True)
    stats = create_stats_dataframe(X)
    print(stats)


if __name__ == "__main__":
    main()
