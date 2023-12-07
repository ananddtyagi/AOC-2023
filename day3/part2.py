
from collections import defaultdict


with open("data.txt") as data:
    
    lines = data.readlines()
    line_len_idx = len(lines[0].strip()) - 1
    
    def get_adjacent_coors(line_n, num_start, num_end):
        adj_coors = []
        gen_coors = lambda line_n, c_range: list((line_n, c_n) for c_n in c_range)
        if line_n > 0:
            adj_coors += gen_coors(line_n-1, range(max(0,num_start-1), min(num_end+1, line_len_idx) + 1))
        if line_n < len(lines)-1: # second to last line and before
            adj_coors += gen_coors(line_n+1, range(max(0,num_start-1), min(num_end+1, line_len_idx) + 1))
        if num_start > 0:
            adj_coors.append((line_n,num_start-1))
        if num_end < line_len_idx-1:
            adj_coors.append((line_n, num_end+1))
        return adj_coors
    
    total = 0
    gears_coors = defaultdict(lambda: {})
    
    for line_n, line in enumerate(lines):
        c_n = 0
        while(c_n <= line_len_idx):
            if line[c_n].isdigit():
                num_start = c_n
                while(line[c_n].isdigit()):
                    c_n+=1                 
                #line[num_start:c_n] is the number
                # check if surrounding contains gear
                adjacent = get_adjacent_coors(line_n, num_start, c_n-1)
                for adj in adjacent:
                    if lines[adj[0]][adj[1]] == "*":
                        if adj[1] in gears_coors[adj[0]]:
                            gears_coors[adj[0]][adj[1]].append(line[num_start:c_n])
                        else:    
                            gears_coors[adj[0]][adj[1]] = [line[num_start:c_n]]
            c_n+=1
        
    for gear_row in gears_coors:
        parts_list = gears_coors[gear_row].values()
        for parts in parts_list:
            if len(parts) == 2:
                total += int(parts[0]) * int(parts[1])
    print(total)
            