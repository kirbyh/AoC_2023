import re
from pathlib import Path

def main(): 
    path = Path(__file__).parent / "../data/01.txt"
    total = 0
    with path.open() as f:
        for l in f.readlines(): 
            digits = [int(s) for s in re.findall(r'\d', l)]
            total += digits[0] * 10 + digits[-1]

    print(total)

if __name__ == '__main__': 
    main()
