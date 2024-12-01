from pathlib import Path
import sys
from collections import Counter

parent_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_directory))

from helper import get_input, get_example  # noqa: E402, F403

DAY = 1


def main():
    input = get_input(DAY)

    first_numbers = []
    last_numbers = []

    for line in input:
        parts = line.split()
        if len(parts) == 2:
            first_numbers.append(int(parts[0]))
            last_numbers.append(int(parts[1]))

    print(f"First numbers: {first_numbers}" f"\nLast numbers: {last_numbers}")

    first_numbers_sorted = sorted(first_numbers)
    last_numbers_sorted = sorted(last_numbers)

    print(f"First numbers sorted: {first_numbers_sorted}" f"\nLast numbers sorted: {last_numbers_sorted}")

    all_differences = []
    for first, last in zip(first_numbers_sorted, last_numbers_sorted):
        diff = abs(last - first)
        all_differences.append(diff)

    print(f"All differences: {all_differences}")

    total_sum = sum(all_differences)
    print(f"Total part 1: {total_sum}")

    right_counts = Counter(last_numbers)
    similarity_score = 0

    for num in first_numbers:
        count_in_right = right_counts.get(num, 0)
        similarity_score += num * count_in_right

    print(f"Total part 2: {similarity_score}")

if __name__ == "__main__":
    main()
