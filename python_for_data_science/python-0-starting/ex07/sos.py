import argparse


def convert_to_morse(text: str, nested_morse: dict):
    """Convert input string to morse."""
    print("".join(nested_morse[c] for c in text))


def main():
    """Main entry point of the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="*")
    parsed = parser.parse_args()

    assert len(parsed.args) == 1, "the arguments are bad"
    assert all(c.isalnum() or c.isspace() for c in parsed.args[0]), \
        "the arguments are bad"

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- "
    }

    convert_to_morse(parsed.args[0].upper(), NESTED_MORSE)


if __name__ == "__main__":
    main()
