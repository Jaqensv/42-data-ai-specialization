import matplotlib.pyplot as plt
from utils.load_csv import load_csv


def display_histogram(y, df) -> None:

    for course in df.columns:
        plt.figure()

        plt.hist(df.loc[y == "Ravenclaw", course], label="Ravenclaw", color="blue", alpha=0.5)
        plt.hist(df.loc[y == "Slytherin", course], label="Slytherin", color="green", alpha=0.5)
        plt.hist(df.loc[y == "Gryffindor", course], label="Gryffindor", color="red", alpha=0.5)
        plt.hist(df.loc[y == "Hufflepuff", course], label="Hufflepuff", color="gold", alpha=0.5)

        plt.title(f"Score distribution by house for {course}")
        plt.xlabel("Notes")
        plt.ylabel("Students")
        plt.legend(title="Hogwarts House")
        plt.show()


def main() -> None:

    y, df = load_csv("data/dataset_train.csv")
    display_histogram(y, df)


if __name__ == "__main__":
    main()