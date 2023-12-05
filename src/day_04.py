from pathlib import Path
from numpy import array, ones

def parse_line(line): 
    card, ret = line.split(":")
    id_num = int(card.split()[1])
    keys, your_nums = ret.split('|')
    return id_num, [int(k) for k in keys.strip().split()], [int(k) for k in your_nums.strip().split()]


def score_line(line, part_b=False): 
    _, keys, nums = parse_line(line)
    total = 0
    for num in nums: 
        if num in keys: 
            if total == 0 or part_b: 
                total += 1
            else: 
                total *= 2
    return total


def parse_stack(lines): 
    num_cards = ones(len(lines)).astype(int)  # keep track of number of each card
    for k, line in enumerate(lines): 
        score = score_line(line, part_b=True)
        num_cards[k+1:k+1+score] += num_cards[k]

    return num_cards


def main(): 
    ans_a = 0
    with open(Path(__file__).parent.parent / 'data/04.txt') as src: 
        lines = [_l.strip() for _l in src.readlines()]
    
    for l in lines: 
        ans_a += score_line(l)
    
    print(ans_a)
    ans_b = parse_stack(lines)
    print(sum(ans_b))

if __name__ == '__main__': 
    main()