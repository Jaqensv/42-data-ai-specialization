from typing import Any


def selection_sort(values) -> list:

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

    if not values:
        return None

    sum_values = 0

    for n in values:
        sum_values += n
    mean = sum_values / len(values)

    return mean


def calculate_median(values) -> float:

    if not values:
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

    if not values:
        return None

    q1 = values[len(values) // 4]
    q3 = values[(len(values) * 3) // 4]

    return [q1, q3]


def calculate_std_deviation(var) -> float:

    if var is None:
        return None

    std = var ** 0.5

    return std


def calculate_variance(values, mean) -> float:

    if not values or mean is None:
        return None

    square_values = 0

    for n in values:
        square_values += (n - mean) ** 2

    var = square_values / len(values)

    return var


def display_results(results, kwargs) -> None:

    for value in kwargs.values():
        if value in results:
            if results[value] is not None:
                print(f"{value} : {results[value]}")
            else:
                print("ERROR")


def ft_statistics(*args: Any, **kwargs: Any) -> None:

    ordered_values = None

    if args:
        ordered_values = selection_sort(args)

    mean = None
    median = None
    quartile = None
    std = None
    var = None

    mean = calculate_mean(ordered_values)
    median = calculate_median(ordered_values)
    quartile = calculate_quartile(ordered_values)
    var = calculate_variance(ordered_values, mean)
    std = calculate_std_deviation(var)

    results = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }

    display_results(results, kwargs)
