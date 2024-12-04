from pathlib import Path
import sys

parent_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_directory))

from helper import get_input  # noqa: E402

DAY = 4

def main():
    input_data = get_input(DAY)
    grid = []
    for line in input_data:
        if line.strip():
            grid.append(list(line.strip()))

    part1_sum = count_xmas_occurrences(grid)
    print(part1_sum)

    part2_sum = count_x_mas_patterns(grid)
    print(part2_sum)

def count_xmas_occurrences(grid):
    count = 0
    word = "XMAS"
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0


    directions = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1)
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(word_length):
                    r = row + i * dr
                    c = col + i * dc
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        found = False
                        break
                    if grid[r][c] != word[i]:
                        found = False
                        break
                if found:
                    count += 1
    return count

def count_x_mas_patterns(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'A':
                nw_row = row - 1
                nw_col = col - 1
                se_row = row + 1
                se_col = col + 1
                if is_valid(nw_row, nw_col, rows, cols) and is_valid(se_row, se_col, rows, cols):
                    nw_letter = grid[nw_row][nw_col]
                    se_letter = grid[se_row][se_col]
                    letters_nw_se = {nw_letter, se_letter}
                    if letters_nw_se == {'M', 'S'}:
                        ne_row = row - 1
                        ne_col = col + 1
                        sw_row = row + 1
                        sw_col = col - 1
                        if is_valid(ne_row, ne_col, rows, cols) and is_valid(sw_row, sw_col, rows, cols):
                            ne_letter = grid[ne_row][ne_col]
                            sw_letter = grid[sw_row][sw_col]
                            letters_ne_sw = {ne_letter, sw_letter}
                            if letters_ne_sw == {'M', 'S'}:
                                count += 1
    return count

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

if __name__ == "__main__":
    main()
