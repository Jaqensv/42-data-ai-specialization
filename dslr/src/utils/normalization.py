import pandas as pd
from utils.math_utils import (
    calculate_mean,
    calculate_variance,
    calculate_std_deviation
)


def normalize_series(values: pd.Series, mean, std) -> pd.Series:
    """Normalizes a given Series from the DataFrame."""

    z_score = pd.Series(dtype=float)

    for index, values in values.items():
        z_score[index] = (values - mean) / std

    return z_score


def normalize_stats(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Fills missing values, computes stats, and normalizes a DataFrame."""

    norm_stats = {}
    norm_df = pd.DataFrame()

    for column in df.columns:
        mean = calculate_mean(df[column].dropna())

        filled_column = df[column].fillna(mean)

        var = calculate_variance(filled_column, mean)
        std = calculate_std_deviation(var)

        norm_stats[column] = {
            "mean": mean,
            "var": var,
            "std": std
        }

        norm_df[column] = normalize_series(filled_column, mean, std)

    return norm_df, norm_stats
