import numpy as np


def validate_family(family, start, end):
    """Handles errors"""

    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not family:
        raise ValueError("Family cannot be empty")
    if not all(isinstance(sublist, list) for sublist in family):
        raise TypeError("Family must contain lists")

    if not (isinstance(start, int) and isinstance(end, int)):
        raise TypeError("Start and End must be int")

    list_len = len(family[0])

    for sublist in family:
        if not sublist:
            raise ValueError("Sublists cannot be empty")
        if len(sublist) != list_len:
            raise ValueError("All sublists must have the same size")

        if not all(isinstance(value, (int, float)) for value in sublist):
            raise TypeError("Sublist must contain int or float values")


def slice_me(family: list, start: int, end: int) -> list:
    """Slices and reshapes a list"""

    validate_family(family, start, end)

    arr = np.array(family)

    print(f"My shape is: {arr.shape}")

    arr = arr[start:end]

    print(f"My new shape is: {arr.shape}")

    return arr.tolist()
