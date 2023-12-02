from pathlib import Path
import re
from math import prod

def parse_text_rgb(l): 
    game = int(re.findall('Game (\d+)', l)[0])  # glean game #
    rgb = {}
    for key in ['red', 'green', 'blue']: 
        rgb[key] = [int(k) for k in re.findall(f'(\d+) {key}', l)]
    
    return game, rgb

def main(): 
    path = Path(__file__).parent / "../data/02.txt"
    total = 0
    with path.open() as f:
        for l in f.readlines(): 
            game, rgb = parse_text_rgb(l)
            mins = [max(rgb[key]) for key in rgb.keys()]
            total += prod(mins)

    print(total)

if __name__ == '__main__': 
    main()