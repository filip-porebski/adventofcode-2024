from pathlib import Path
import sys

parent_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_directory))

from helper import get_input, get_example  # noqa: E402, F403

DAY = 1


def main():
    print(get_input(DAY))
    print(get_example(DAY, 1))


if __name__ == "__main__":
    main()
