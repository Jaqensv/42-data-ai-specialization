import matplotlib.pyplot as plt
import pandas as pd
from utils.load_csv import load_csv


def display_histogram(df: pd.DataFrame, houses: pd.Series) -> None:
    """Displays the score distribution by house for the selected course."""

    course = "Care of Magical Creatures"

    plt.figure()

    plt.hist(df.loc[houses == "Ravenclaw", course], label="Ravenclaw", color="blue", alpha=0.5)
    plt.hist(df.loc[houses == "Slytherin", course], label="Slytherin", color="green", alpha=0.5)
    plt.hist(df.loc[houses == "Gryffindor", course], label="Gryffindor", color="red", alpha=0.5)
    plt.hist(df.loc[houses == "Hufflepuff", course], label="Hufflepuff", color="gold", alpha=0.5)

    plt.title(f"Score distribution by house for {course}")
    plt.xlabel("Notes")
    plt.ylabel("Students")
    plt.legend(title="Hogwarts House")
    plt.show()


def main() -> None:
    """Loads the training dataset and displays the selected histogram."""

    y, df = load_csv("data/dataset_train.csv")
    display_histogram(df, y)


if __name__ == "__main__":
    main()