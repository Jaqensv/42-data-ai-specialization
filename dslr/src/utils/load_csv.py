import pandas as pd
import os
from typing import Optional


def load_csv(
    dataset: str, training: bool
) -> tuple[Optional[pd.Series], Optional[pd.DataFrame]]:
    """Loads and cleans a training or test dataset."""

    if not os.path.exists(dataset):
        print(f"ERROR : file {dataset} does not exist.")
        return None, None

    try:
        df = pd.read_csv(dataset)
    except Exception as error:
        print(f"Error loading csv: {error}")
        return None, None

    if df.empty:
        print("Dataset is empty.")
        return None, None

    y = None

    if training:
        df = df.dropna().reset_index(drop=True)
        y = df["Hogwarts House"]
    else:
        df = df.reset_index(drop=True)

    df = df.drop(columns=[
        "Hogwarts House",
        "Index",
        "First Name",
        "Last Name",
        "Birthday",
        "Best Hand"
    ])

    X = df

    return y, X
