import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="*")
    parsed = parser.parse_args()

    assert len(parsed.args) == 1, "more than one argument is provided"
    assert parsed.args[0].lstrip("-").isdigit(), "argument is not an integer"

    number = int(parsed.args[0])

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
