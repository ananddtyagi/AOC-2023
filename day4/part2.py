import numpy as np

with open("data.txt", "r") as data:
    lines = data.readlines()
    copies = np.ones(len(lines))
    print(copies)
    def num_wins(winning_nums, my_nums):
        win_dict = {}
        for wn in winning_nums:
            win_dict[wn] = 1
        win_count = 0
        for mn in my_nums:
            if mn in win_dict:
                # that's a winner
                win_count +=1
        return win_count
    
    for i, line in enumerate(lines):
        card_info, numbers = line.split(":")
        winning_nums, my_nums = numbers.strip().split(" | ")
        
        to_int = lambda x: int(x)
        
        winning_nums = list(map(to_int, winning_nums.split()))
        my_nums = list(map(to_int, my_nums.split()))

        win_count = num_wins(winning_nums, my_nums)
        if win_count > 0:
            copies[i+1:i+1+win_count] += copies[i]
    print(sum(copies))