from collections import defaultdict
import numpy as np
import time
import pickle as pkl
start = time.time()
last = start
with open("data.txt") as data:
    lines = data.readlines()
    instructions = lines[0].strip()
    
    nodes = {}
    curr_nodes = []
    
    for line in lines[2:]:
        node = line[:3]
        left = line[7:10]
        right = line[12:15]
        
        nodes[node] = {"L": left, "R": right}
        if node[2] == "A":
            curr_nodes.append(node)
    
for start_node in curr_nodes:
    node = start_node
    visited = defaultdict(lambda: -1)
    count = 0
    time_count = 0
    # print(int(11795205644011/10000000))
    while visited[node] != (count % len(instructions)):
        visited[node] = count % len(instructions)
        node = nodes[node][instructions[count % len(instructions)]]
        count+=1
        if count % (int(11795205644011/10000000)) == 0:
            now = time.time()
            last = now
            time_count +=1 

            with open(f"progress_start_{start_node}.pkl","wb+") as pkl_f:
                data = {"count": count, "visited": dict(visited), "curr_node": node}
                pkl.dump(data, pkl_f)

    print(count)

"""
Notes:

So, the LCM technique works and I confirmed there's no loops that could tell us if that LCM result was wrong.
If we had found a loop for any of the starting points where the LCM of those loops was less than the answer LCM then
we'd find a correct solution that's earlier than the accepted solution.
I got 23590411288022 which is double the answer 11795205644011. Meaning the 11795205644011 answer is in fact the earliest stopping point
"""