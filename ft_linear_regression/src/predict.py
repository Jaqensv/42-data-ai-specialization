import train
import utils
import matplotlib.pyplot as plt
import os

def parse_model(model_text):
    params = {}

    for line in model_text:
        key, value = line.strip().split("=")
        params[key] = value

    try:
        theta0 = float(params["theta0"])
        theta1 = float(params["theta1"])
        max_mileage = float(params["max_mileage"])
    except ValueError:
        printf("Model parsing conversion error")

    return theta0, theta1, max_mileage

def predict_price(mileage):
    try:
        with open("src/models/model.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No model found. Please train the model first")

    theta0, theta1, max_mileage = parse_model(lines)

    estimated_price = utils.estimate_price(theta0, theta1, mileage / max_mileage)
    if estimated_price < 0:
        estimated_price = 0

    print(f"Estimate price for {int(mileage)} km = {int(estimated_price)}€")

    return estimated_price

def main():
    while True:
        try:
            mileage = float(input("Enter mileage: "))
            if mileage < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter valid number")

    estimated_price = predict_price(mileage)

if __name__ == "__main__":
    main()
