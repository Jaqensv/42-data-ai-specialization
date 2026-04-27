import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_chart(df_life, df_incm) -> None:
    """Displays a chart from a dataframe"""

    try:
        data = pd.DataFrame({
            "incm": df_incm["1900"],
            "life": df_life["1900"].astype(float)
        })
    except ValueError:
        print("Error: invalid numeric data")
        return

    data = data.dropna()

    if data.empty:
        print("Error: no valid data for year 1900")
        return

    x = data["incm"]
    y = data["life"]

    plt.scatter(x, y)
    plt.xlim(300, 11000)
    plt.xscale("log")
    plt.xticks(
        [300, 1000, 10000],
        ["300", "1k", "10k"]
    )
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()


def main():
    """Main calling load and display_chart"""

    df_life = load("life_expectancy_years.csv")
    df_incm = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if df_life is None or df_incm is None:
        print("Error: dataset could not be loaded")
        return

    display_chart(df_life, df_incm)


if __name__ == "__main__":
    main()
