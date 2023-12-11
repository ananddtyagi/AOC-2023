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
        
    count = 0
    def all_end_in_Z():
        for node in curr_nodes: 
            if node[2] != "Z":
                return False
        return True
        
    while not all_end_in_Z():
        instruction = instructions[count % len(instructions)]
        for i in range(len(curr_nodes)):
            curr_nodes[i] = nodes[curr_nodes[i]][instruction]
        count+=1
    print(count)