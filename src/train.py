import utils

def write_model(theta0, theta1, max_mileage):
    with open("src/models/model.txt", "w") as f:
        f.write(f"theta0={theta0}\n")
        f.write(f"theta1={theta1}\n")
        f.write(f"max_mileage={max_mileage}\n")

def train_model():
    mileage, price = utils.read_csv() # lecture csv
    m = len(mileage)
    theta0 = 0.0
    theta1 = 0.0
    learning_rate = 0.5

    raw_mileage = mileage.copy()
    max_mileage = max(mileage)                         # normalisation
    mileage = [km / max_mileage for km in raw_mileage] # normalisation

    for epoch in range(1000):
        tmp0 = 0.0
        tmp1 = 0.0

        for i in range (m):
            tmp0 += utils.estimate_price(theta0, theta1, mileage[i]) - price[i]
            tmp1 += (utils.estimate_price(theta0, theta1, mileage[i]) - price[i]) * mileage[i]

        tmp0 = learning_rate * (1 / m) * tmp0
        tmp1 = learning_rate * (1 / m) * tmp1
        theta0 = theta0 - tmp0 # correction
        theta1 = theta1 - tmp1 # correction

    x = raw_mileage
    y = [utils.estimate_price(theta0, theta1, km / max_mileage) for km in raw_mileage]

    utils.display_plt(x, y, raw_mileage, price) # display graph
    write_model(theta0, theta1, max_mileage)

if __name__ == "__main__":
    train_model()
