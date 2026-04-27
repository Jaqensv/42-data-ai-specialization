import matplotlib.pyplot as plt
from load_csv import load


def convert(values):
    """Removes M and k and normalizes the values"""

    if "M" in values:
        return float(values.replace("M", ""))
    if "k" in values:
        return float(values.replace("k", "")) / 1_000

    return float(values)


def display_chart(df):
    """Displays a chart from a dataframe"""

    france = df.loc[df.eq("France").any(axis=1)]
    venezuela = df.loc[df.eq("Venezuela").any(axis=1)]

    if france.empty or venezuela.empty:
        print("Error: France or Venezuela not found")
        return

    x = df.columns[1:].astype(int)
    y = france.iloc[0, 1:]
    y2 = venezuela.iloc[0, 1:]
    y = y.apply(convert)
    y2 = y2.apply(convert)

    plt.plot(x, y, label="France")
    plt.plot(x, y2, label="Venezuela")
    plt.xlim(1800, 2050)
    plt.ylim(0, 80)
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.yticks([20, 40, 60], ["20M", "40M", "60M"])

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.show()


def main():
    """Main calling load and display_chart"""

    df = load("population_total.csv")

    if df is None:
        print("Error: dataset could not be loaded")
        return

    display_chart(df)


if __name__ == "__main__":
    main()
