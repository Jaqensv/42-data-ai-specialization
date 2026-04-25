import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Creates a dataframe from a csv"""

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        return None
    except pd.errors.EmptyDataError:
        return None
    except pd.errors.ParserError:
        return None
    except PermissionError:
        return None
