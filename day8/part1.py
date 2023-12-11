with open("data.txt") as data:
    lines = data.readlines()
    instructions = lines[0].strip()
    
    nodes = {}
    
    for line in lines[2:]:
        node = line[:3]
        left = line[7:10]
        right = line[12:15]
        
        nodes[node] = {"L": left, "R": right}
        
    curr = "AAA"
    count = 0
    
    while curr != "ZZZ":
        curr = nodes[curr][instructions[int(count%len(instructions))]]
        count+=1
    print(count)
    