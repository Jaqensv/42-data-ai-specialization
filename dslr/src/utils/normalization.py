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
    """Calculates the mean, var and std and normalizes a given DataFrame."""

    norm_stats = {}
    norm_df = pd.DataFrame()

    for column in df.columns:
        mean = calculate_mean(df[column])
        var = calculate_variance(df[column], mean)
        std = calculate_std_deviation(var)
        norm_stats[column] = {
            "mean": mean,
            "var": var,
            "std": std       
        }
        norm_df[column] = normalize_series(
            df[column], 
            norm_stats[column]["mean"], 
            norm_stats[column]["std"]
        )

    return norm_df, norm_stats
