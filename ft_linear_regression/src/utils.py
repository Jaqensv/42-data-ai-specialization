import csv
import matplotlib.pyplot as plt

def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

def read_csv():
    with open("data/data.csv", newline="", encoding="utf-8") as file:
        mileage = []
        price = []
        reader = csv.DictReader(file)

        for row in reader:
            mileage.append(float(row["km"]))
            price.append(float(row["price"]))

    return mileage, price

def display_plt(x, y, raw_mileage, price):
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price (€)")
    plt.title("Linear progression")
    plt.scatter(raw_mileage, price, color="green", s=20)
    plt.plot(raw_mileage, y)
    plt.show()
