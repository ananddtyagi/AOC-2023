import numpy as np
import time

start = time.time()

class Node:
    def __init__(self, value: str):
        self.value = value
        
    def setL(self, left_node):
        self.l = left_node
    
    def setR(self, right_node):
        self.r = right_node
    
    def __repr__(self):
        return self.value 
    # + " " + self.l.value + " " + self.r.value
        
with open("data.txt") as data:
    lines = data.readlines()
    instructions = lines[0].strip()
    
    node_data = {}
    nodes = {}
    curr_nodes = []
    
    for line in lines[2:]:
        node = line[:3]
        left = line[7:10]
        right = line[12:15]
        
        node_data[node] = {"L": left, "R": right}
        nodes[node] = Node(node)
        if node[2] == "A":
            curr_nodes.append(nodes[node])
        
    for node_val, node in nodes.items():
        node.setL(nodes[node_data[node_val]["L"]])
        node.setR(nodes[node_data[node_val]["R"]])
        
    count = 0
    def all_end_in_Z():
        for node in curr_nodes: 
            if node.value[2] != "Z":
                return False
        return True
        
    counts = [0]*len(curr_nodes)
    counts_set = [0]*len(curr_nodes)
    while not sum(counts_set) == len(curr_nodes):        
        instruction = instructions[count % len(instructions)]
        for i in range(len(curr_nodes)):
            if curr_nodes[i].value[2] == "Z" and counts_set[i] == 0:
                counts[i] = count
                counts_set[i] = 1
            elif counts[i] == 0:
                if instruction == "L":
                    curr_nodes[i] = curr_nodes[i].l
                else:
                    curr_nodes[i] = curr_nodes[i].r
        count+=1
    print(counts)
    # the only reason you can use lcm here is due to luck.
    # there is really nothing in the problem indicating that each path from starting A to first Z
    # is the exit node it will eventually hit to exit, which LCM assumes. In fact, each exit isn't even a loop back to the starting node.
    print(np.lcm.reduce(counts))

print(time.time() - start)
