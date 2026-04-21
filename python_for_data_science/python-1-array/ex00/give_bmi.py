import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""

    if len(height) != len(weight):
        raise ValueError("Lists must have the same size")

    if not all(isinstance(x, (int, float)) for x in height + weight):
        raise TypeError("All elements must be int or float")

    if any(h == 0 for h in height):
        raise ValueError("Height cannot be zero")

    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr ** 2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans where BMI exceeds the limit."""

    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("BMI list must contain numbers")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    bmi_arr = np.array(bmi)

    filter_arr = bmi_arr > limit

    return filter_arr.tolist()
