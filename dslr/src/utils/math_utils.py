import pandas as pd
from math import exp


def calculate_sigmoid(z: float) -> float:
    """Applies the sigmoid function to a score."""

    return 1 / (1 + exp(-z))


def selection_sort(values) -> list:
    """Sorts the values using the selection sort algorithm."""

    new_values = []
    for value in values:
        new_values += [value]

    i = 0

    for _ in new_values:
        min_index = i
        j = i + 1

        for _ in new_values[i + 1:]:
            if new_values[j] < new_values[min_index]:
                min_index = j
            j += 1

        new_values[i], new_values[min_index] = (
            new_values[min_index],
            new_values[i]
        )
        i += 1

    return new_values


def calculate_mean(values) -> float:
    """Calculates the arithmetic mean of the values."""

    if len(values) == 0:
        return None

    sum_values = 0

    for n in values:
        sum_values += n
    mean = sum_values / len(values)

    return mean


def calculate_median(values) -> float:
    """Calculates the median of the values."""

    if len(values) == 0:
        return None

    median = 0

    if len(values) % 2 != 0:
        median = values[int(len(values) // 2)]
    else:
        median = (
            values[int(len(values) // 2) - 1]
            + values[int(len(values) // 2)]
        ) / 2

    return median


def calculate_quartile(values) -> list[float]:
    """Calculates the first and third quartiles."""

    if len(values) == 0:
        return None

    q1 = values[len(values) // 4]
    q2 = values[len(values) // 2]
    q3 = values[(len(values) * 3) // 4]

    return [q1, q2, q3]


def calculate_std_deviation(var) -> float:
    """Calculates the standard deviation from the variance."""

    if var is None:
        return None

    std = var ** 0.5

    return std


def calculate_variance(values, mean) -> float:
    """Calculates the variance of the values."""

    if len(values) == 0 or mean is None:
        return None

    square_values = 0

    for n in values:
        square_values += (n - mean) ** 2

    var = square_values / len(values)

    return var


def calculate_min_max(values) -> float:
    """Calculate min and max values from the given Series."""

    if len(values) == 0:
        return None, None

    min_value = None

    for n in values:
        if min_value is None:
            min_value = n
        max_value = n

    return min_value, max_value


def calculate_stats(values: pd.Series) -> tuple[float | int]:
    """Calculates and displays statistics from the given dataframe."""

    ordered_values = None

    if not values.empty:
        ordered_values = selection_sort(values)

    mean = None
    quartile = None
    std = None
    var = None
    min_value = None
    max_value = None

    mean = calculate_mean(ordered_values)
    quartile = calculate_quartile(ordered_values)
    var = calculate_variance(ordered_values, mean)
    std = calculate_std_deviation(var)
    min_value, max_value = calculate_min_max(ordered_values)

    return mean, quartile, std, min_value, max_value
