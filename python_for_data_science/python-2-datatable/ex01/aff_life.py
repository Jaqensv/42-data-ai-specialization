from load_csv import load
import matplotlib.pyplot as plt


def display_chart(df):
    """Displays a chart from a dataframe"""

    france = df.loc[df.eq("France").any(axis=1)]

    if france.empty:
        print("Error: France not found")
        return

    x = df.columns[1:].astype(int)
    y = france.iloc[0, 1:].astype(float)

    plt.plot(x, y)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(x[::40])
    plt.show()


def main():
    """Calls fonctions load and display_chart"""

    df = load("life_expectancy_years.csv")

    if df is None:
        print("Error: dataset could not be loaded")
        return

    display_chart(df)


if __name__ == "__main__":
    main()
