import matplotlib.pyplot as plt
import pandas as pd
from itertools import combinations
from math import sqrt

from utils.load_csv import load_csv
from utils.math_utils import calculate_mean


def calculate_correlation(courses: pd.DataFrame) -> tuple[str | None, str | None]:
    """Returns the pair of courses with the highest absolute Pearson correlation."""

    if courses.empty or len(courses.columns) < 2:
        print("Not enough course data to calculate correlations.")
        return None, None

    score = 0
    best_course_1 = None
    best_course_2 = None

    for course_1, course_2 in combinations(courses.columns, 2):
        mean_x = calculate_mean(courses[course_1])
        mean_y = calculate_mean(courses[course_2])

        numerator = 0
        sum_x = 0
        sum_y = 0

        for index in courses.index:
            x = courses.loc[index, course_1]
            y = courses.loc[index, course_2]

            dx = x - mean_x
            dy = y - mean_y

            numerator += dx * dy
            sum_x += dx ** 2
            sum_y += dy ** 2

        denominator = sqrt(sum_x * sum_y)

        if denominator == 0:
            continue

        correlation = numerator / denominator

        if abs(correlation) > score:
            score = abs(correlation)
            best_course_1 = course_1
            best_course_2 = course_2

    return best_course_1, best_course_2


def display_scatter_plot(
    courses: pd.DataFrame,
    course_1: str,
    course_2: str
) -> None:
    """Displays a scatter plot for the two selected correlated courses."""

    if course_1 not in courses.columns or course_2 not in courses.columns:
        print("Selected courses are missing from the dataframe.")
        return

    x = courses[course_1]
    y = courses[course_2]

    plt.scatter(x, y)
    plt.title(f"Correlation between {course_1} and {course_2}")
    plt.xlabel(course_1)
    plt.ylabel(course_2)
    plt.show()


def main() -> None:
    """Loads the dataset and displays the most correlated course pair."""

    _, courses = load_csv("data/dataset_train.csv")

    if courses is None or courses.empty:
        print("No course data available.")
        return

    course_1, course_2 = calculate_correlation(courses)

    if course_1 is None or course_2 is None:
        print("Unable to find a correlated pair of courses.")
        return

    display_scatter_plot(courses, course_1, course_2)


if __name__ == "__main__":
    main()
