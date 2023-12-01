import re
from pathlib import Path

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
re_search = r'\d' + r''.join(['|' + key for key in numbers.keys()])
rev_search = r'\d' + r''.join('|' + key[::-1] for key in numbers.keys())

def to_int(s): 
    if s in numbers.keys(): 
        return numbers[s]
    elif s.isnumeric(): 
        return int(s)
    else: 
        raise ValueError(f'Value {s} is not an integer.')

def str_to_number(s): 
    parsed = re.findall(re_search, s)
    parsed_rev = re.findall(rev_search, s[::-1])
    return to_int(parsed[0]) * 10 + to_int(parsed_rev[0][::-1])

def main(): 
    path = Path(__file__).parent / "../data/01.txt"
    total = 0
    with path.open() as f:
        for l in f.readlines(): 
            total += str_to_number(l)

    print(total)

if __name__ == '__main__': 
    main()
