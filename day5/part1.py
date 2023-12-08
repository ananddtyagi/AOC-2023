with open("data.txt") as data:
    
    lines = data.readlines();
    
    curr_state = list(map(lambda x: int(x), lines[0][6:].split()))
    modified = [False] * len(curr_state)
    
    for line in lines[1:]:
        if line == "\n":
            modified = [False] * len(curr_state)
            continue
        if line[0].isdigit():
            dest_r_start, source_r_start, range_len = line.split()
            for i, state in enumerate(curr_state):
                if not modified[i]:
                    if state >= int(source_r_start) and state < int(source_r_start) + int(range_len):
                        modified[i] = True
                        curr_state[i] = int(dest_r_start) + (state - int(source_r_start))
    print(min(curr_state))