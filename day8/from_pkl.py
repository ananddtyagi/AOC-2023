
from collections import defaultdict
import pickle as pkl

with open("progress.pkl", "rb") as progress:
    data_progress = pkl.load(progress)
print(data_progress)

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
    
# for start_node in curr_nodes:
print(data_progress)
node = data_progress['curr_node']
visited = defaultdict(lambda: -1, data_progress['visited'], )
count = data_progress['count']
time_count = 0
# print(int(11795205644011/10000000))
while visited[node] != (count % len(instructions)):
    visited[node] = count % len(instructions)
    node = nodes[node][instructions[count % len(instructions)]]
    count+=1
    # if count % (int(11795205644011/10000000)) == 0:
    if count == 5:
        now = time.time()
        last = now
        time_count +=1 

        with open("progress.pkl","wb+") as pkl_f:
            data = {"count": count, "visited": dict(visited), "curr_node": node}
            pkl.dump(data, pkl_f)
print(count)
