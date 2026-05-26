import pandas as pd


def load_csv(
    dataset: str, training: bool
) -> tuple[pd.Series | None, pd.DataFrame | None]:
    """Loads and cleans a training or test dataset."""

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
