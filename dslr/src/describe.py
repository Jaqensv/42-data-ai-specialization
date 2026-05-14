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

    y, X = load_csv("data/dataset_train.csv")
    stats = create_stats_dataframe(X)
    print(stats)


if __name__ == "__main__":
    main()





#$> describe.[extension] dataset_train.csv
#Feature 1 Feature 2 Feature 3 Feature 4
#Count 149.000000 149.000000 149.000000 149.000000
#Mean 5.848322 3.051007 3.774497 1.205369
#Std 5.906338 3.081445 4.162021 1.424286
#Min 4.300000 2.000000 1.000000 0.100000
#25% 5.100000 2.800000 1.600000 0.300000
#50% 5.800000 3.000000 4.400000 1.300000
#75% 6.400000 3.300000 5.100000 1.800000
#Max 7.900000 4.400000 6.900000 2.500000