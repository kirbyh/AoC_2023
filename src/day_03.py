from pathlib import Path
import re 

symbols = '*-%$=@#/&+'
gears = '*'

def check_adjacent(number_pos, symbol_pos): 
    ret = []
    N = len(number_pos)
    for k, line in enumerate(number_pos): 
        for element in line: 
            col, val = element
            n = len(val)
            # check adjacent values
            for j in range(max(k - 1, 0), min(k + 2, N)): 
                if any([_col in symbol_pos[j] for _col in range(max(col - 1, 0), col + n + 1)]): 
                    ret.append(int(val))
                    break
    return ret

def check_gears(number_pos, gear_pos): 
    ret = []
    N = len(number_pos)
    for row, gears in enumerate(gear_pos): 
        for col in gears: 
            adjacent = []
            for _row in range(max(row - 1, 0), min(row + 2, N)): 
                # check adjacent numbers
                for element in number_pos[_row]: 
                    _col, val = element
                    if col in range(_col-1, _col + len(val) + 1): 
                        adjacent.append(int(val))
            if len(adjacent) == 2: 
                ret.append(adjacent[0] * adjacent[1])
    return ret

def main(): 
    with open(Path(__file__).parent.parent / 'data/03.txt') as src: 
        symbol_pos = []
        gear_pos = []
        number_pos = []
        for l in src.readlines(): 
            symbol_pos.append([k for k, char in enumerate(l.strip()) if char in symbols])
            gear_pos.append([k for k, char in enumerate(l.strip()) if char in gears])
            tmp = [(m.start(), m.groups()[0]) for m in re.finditer('(\d+)', l.strip())]
            number_pos.append(tmp)  # store number and its starting index

        ret = check_adjacent(number_pos, symbol_pos)        
        print(sum(ret))  # part 1

        ret = check_gears(number_pos, gear_pos)
        print(sum(ret))  # part 2

if __name__ == '__main__': 
    main()
