import pandas as pd


def load_csv(dataset: str) -> tuple[pd.Series, pd.DataFrame]:
    """Loads and cleans up the dataset by dropping irrelevant columns."""

    try:
        df = pd.read_csv(dataset)
    except Exception as error:
        print(f"Error loading csv: {error}")
        return None, None

    if df.empty:
        print("Dataset is empty.")
        return None, None

    df = df.dropna()

    y = df["Hogwarts House"]

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
