from utils.load_csv import load_csv
from utils.normalization import normalize_stats


def main() -> None:

    y, X = load_csv("data/dataset_train.csv")
    X, norm_stats = normalize_stats(X)
    #train model

if __name__ == "__main__":
    main()