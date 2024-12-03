import re
from pathlib import Path
import sys
from html import unescape

parent_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_directory))

from helper import get_input, get_example  # noqa: E402, F403

DAY = 3

def mul(x, y, enabled=True):
    """Multiply x and y if multiplication is enabled."""
    if enabled:
        return int(x) * int(y)
    return 0

def main():
    raw_input = get_input(DAY, 1)
    
    if isinstance(raw_input, list):
        section = ''.join(raw_input)
    else:
        section = raw_input
    
    section = unescape(section)
    exp = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|\b(do|don't)\(\)")
    
    part1_sum = 0
    part2_sum = 0
    enabled = True
    
    for match in exp.findall(section):
        x, y, instruction = match
        
        # Part 1
        if x and y:
            part1_sum += mul(x, y)
        
        # Part 2
        if instruction == "do":
            enabled = True
        elif instruction == "don't":
            enabled = False
        elif x and y:
            part2_sum += mul(x, y, enabled)
    
    print(f"Total sum for Part 1: {part1_sum}")
    print(f"Total sum for Part 2: {part2_sum}")

if __name__ == "__main__":
    main()
