from pathlib import Path
import sys

parent_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_directory))

from helper import get_input, get_example  # noqa: E402, F403

DAY = 2


def is_safe(digits):
    is_increasing = True
    is_decreasing = True
    valid_differences = True

    for i in range(len(digits) - 1):
        diff = digits[i + 1] - digits[i]

        if diff > 0:
            is_decreasing = False
        elif diff < 0:
            is_increasing = False

        if not (1 <= abs(diff) <= 3):
            valid_differences = False

    return valid_differences and (is_increasing or is_decreasing)


def can_be_safe_with_removal(digits):
    for i in range(len(digits)):
        modified_digits = digits[:i] + digits[i + 1 :]
        if is_safe(modified_digits):
            return True
    return False


def main():
    input_data = get_input(DAY)

    part1_sum = 0
    part2_sum = 0

    for row_index, row in enumerate(input_data):
        # print(f"Processing row {row_index + 1}: {row}")

        digits = list(map(int, row.split()))
        if is_safe(digits):
            part1_sum += 1
            part2_sum += 1
        elif can_be_safe_with_removal(digits):
            part2_sum += 1

    # Print the results
    print(f"\nPart 1: Total safe rows (part 1): {part1_sum}")
    print(f"Part 2: Total safe rows (part 2): {part2_sum}")


if __name__ == "__main__":
    main()
