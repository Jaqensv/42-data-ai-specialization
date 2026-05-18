import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from utils.load_csv import load_csv


def display_pair_plot(houses: pd.Series, courses: pd.DataFrame) -> None:
    """Displays a pair plot of course scores colored by Hogwarts house."""

    if houses is None or courses is None:
        print("Missing data for pair plot.")
        return

    if houses.empty or courses.empty:
        print("Pair plot data is empty.")
        return

    if len(houses) != len(courses):
        print("Houses and courses do not have the same number of rows.")
        return

    df = courses.copy()
    df["Hogwarts House"] = houses

    house_colors = {
        "Gryffindor": "red",
        "Hufflepuff": "gold",
        "Ravenclaw": "blue",
        "Slytherin": "green"
    }

    df = df.rename(columns={
        "Arithmancy": "Arith.",
        "Astronomy": "Astro.",
        "Herbology": "Herbo.",
        "Defense Against the Dark Arts": "Defense",
        "Divination": "Divin.",
        "Muggle Studies": "Muggle",
        "Ancient Runes": "Runes",
        "History of Magic": "History",
        "Transfiguration": "Transfig.",
        "Care of Magical Creatures": "Creatures"
    })

    grid = sns.pairplot(
        data=df,
        hue="Hogwarts House",
        palette=house_colors,
        corner=True,
        height=3,
        plot_kws={"s": 12, "alpha": 0.6}
    )

    for row in grid.axes:
        for ax in row:
            if ax is not None:
                ax.tick_params(axis="both", labelsize=7)
                ax.xaxis.set_major_locator(MaxNLocator(3))
                ax.yaxis.set_major_locator(MaxNLocator(3))

    grid.fig.subplots_adjust(
        left=0.10,
        bottom=0.08
    )
    grid.fig.align_ylabels()

    plt.show()


def main() -> None:
    """Loads the training dataset and displays its course pair plot."""

    houses, courses = load_csv("data/dataset_train.csv")

    if houses is None or courses is None:
        return

    display_pair_plot(houses, courses)


if __name__ == "__main__":
    main()
