import argparse
import string


def count_characters(text: str, counters: dict):
    """Count characters provided by the user."""
    for c in text:
        if c.isupper():
            counters["upper"] += 1
        if c.islower():
            counters["lower"] += 1
        if c in string.punctuation:
            counters["punct"] += 1
        if c.isspace():
            counters["space"] += 1
        if c.isdigit():
            counters["digit"] += 1


def main():
    """Main entry point of the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="*")
    parsed = parser.parse_args()

    assert len(parsed.args) <= 1, "more than one argument is provided"
    text = ""
    if parsed.args:
        text = parsed.args[0]
    while not text:
        text = input("Please provide a string: ")

    counters = {
        "upper": 0,
        "lower": 0,
        "punct": 0,
        "space": 0,
        "digit": 0
    }

    count_characters(text, counters)

    print(f"The text contains {len(text)} characters:")
    print(f"{counters['upper']} upper letters")
    print(f"{counters['lower']} lower letters")
    print(f"{counters['punct']} punctuation marks")
    print(f"{counters['space']} spaces")
    print(f"{counters['digit']} digits")


if __name__ == "__main__":
    main()
