from pathlib import Path
import re

def parse_text_rgb(l): 
    game = int(re.findall('Game (\d+)', l)[0])  # glean game #
    rgb = {}
    for key in ['red', 'green', 'blue']: 
        rgb[key] = [int(k) for k in re.findall(f'(\d+) {key}', l)]
    
    return game, rgb


def main(): 
    limit = dict(red=12, green=13, blue=14)  # max number of each color
    path = Path(__file__).parent / "../data/02.txt"
    total = 0
    with path.open() as f:
        for l in f.readlines(): 
            game, rgb = parse_text_rgb(l)
            if all([max(rgb[key]) <= limit[key] for key in limit.keys()]): 
                total += game

    print(total)

if __name__ == '__main__': 
    main()