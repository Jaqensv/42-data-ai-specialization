import utils
from predict import predict_price
import csv

def calculate_mean_absolute_error():
    mileage, price = utils.read_csv()
    m = len(mileage)
    error = 0

    for i in range(m):
        estimated_price = predict_price(mileage[i])
        error += abs((estimated_price - price[i]))
    error /= m

    return error
    
def main():
    error = calculate_mean_absolute_error()
    print(f"Mean absolute error = {error:.2f}€")

if __name__ == "__main__":
    main()