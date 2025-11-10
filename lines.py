import sys


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    loc = count_lines_of_code(lines)
    print(loc)


def count_lines_of_code(lines):
    """Counts lines of code excluding comments and blank lines."""
    loc = 0

    for line in lines:
        stripped = line.lstrip()
        # Exclude blank lines and lines that start with #
        if stripped and not stripped.startswith("#"):
            loc += 1

    return loc


if __name__ == "__main__":
    main()