
import numpy as np

data = open("data.txt").read().splitlines()
    
    
def add_num(layers, num):
    layers[0].append(num)
    for i in range(1, len(layers)):
        layers[i].append(layers[i-1][-1] - layers[i-1][-2])
    return layers

def next_layer_compute(layer):
    next_layer = []
    for i in range(1, len(layer)):
        next_layer.append(layer[i] - layer[i-1])
    return next_layer
    
def get_pattern_depth(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    layers = [nums[:4]]
    i = 3
    while i < len(nums): # while you don't reach constant val
        layers.append(next_layer_compute(layers[-1]))
        if layers[-1][0] == layers[-1][1] == layers[-1][2]:
            break
        add_num(layers, nums[i])
        i+=1
    return len(layers)
        
def compute_last(pattern_depth, nums, num_predict):
    coef_pattern =  np.array([[pd**i for i in range(pattern_depth-1,-1,-1)] for pd in range(1, pattern_depth+1)], dtype=float)
    vals = np.array(nums, dtype=float)
    print(coef_pattern)
    coefs = np.linalg.solve(coef_pattern, vals)
    next_val = 0
    for i in range(0, len(coefs)):
        next_val += coefs[len(coefs)-i-1]*num_predict**i
    
    return np.round(next_val)

next_val = []
for line in data:
    nums = line.split()
    pattern_depth = get_pattern_depth(nums)
    last = compute_last(pattern_depth, nums[:pattern_depth], len(nums)+1)
    next_val.append(last)
    print(last)
print(sum(next_val))