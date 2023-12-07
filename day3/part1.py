

with open("data.txt") as data:
    lines = data.readlines();
    line_len_idx = len(lines[0].strip()) - 1
    
    def get_adjacent(line_n, num_start, num_end):
        adj = []
        if line_n > 0:
            adj += lines[line_n-1][max(0,num_start-1): min(num_end+1, line_len_idx) + 1]
        if line_n < len(lines)-1: # second to last line and before
            adj += lines[line_n+1][max(0,num_start-1): min(num_end+1, line_len_idx) + 1]
        if num_start > 0:
            adj.append(lines[line_n][num_start-1])
        if num_end < line_len_idx-1:
            adj.append(lines[line_n][num_end+1])
        return adj
    
    def isSpecial(ch):
        return not (ch == "." or ch.isdigit())

    def has_special(l):
        return any(isSpecial(i) for i in l)
            
    total = 0
    for line_n, line in enumerate(lines):
        c_n=0
        while (c_n <= line_len_idx):
            if line[c_n].isdigit():
                num_start = c_n
                while(line[c_n].isdigit()):
                    c_n+=1
                adjacent = get_adjacent(line_n, num_start, c_n-1)
                if has_special(adjacent):
                    total += int(line[num_start: c_n])
            c_n+=1
    print(total)