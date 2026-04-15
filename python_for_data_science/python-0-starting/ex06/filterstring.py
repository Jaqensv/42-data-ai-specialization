from ft_filter import ft_filter
import argparse


def main():
    """Main entry point of the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="*")
    parsed = parser.parse_args()

    assert len(parsed.args) == 2, "the arguments are bad."
    assert len(parsed.args[0]) > 0, "the first argument cannot be empty."
    assert all(c.isalnum() or c == " " for c in parsed.args[0]), \
        "the first argument must not contain special or invisible characters."
    assert parsed.args[1].lstrip("-").isdigit(), \
        "the second argument is not an integer."

    x = parsed.args[0].split()
    n = int(parsed.args[1])
    filtered_list = ft_filter(lambda x: len(x) > n, x)

    print(filtered_list)


if __name__ == "__main__":
    main()
