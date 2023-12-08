

with open("data.txt", "r") as data:
    total = 0
    for line in data:
        card_info, numbers = line.split(":")
        winning_nums, my_nums = numbers.strip().split(" | ")
        
        to_int = lambda x: int(x)
        
        winning_nums = list(map(to_int, winning_nums.split()))
        my_nums = list(map(to_int, my_nums.split()))
        
        win_dict = {}
        for wn in winning_nums:
            win_dict[wn] = 1
        win_count = 0
        for mn in my_nums:
            if mn in win_dict:
                # that's a winner
                win_count +=1
        if win_count > 0:
            total+=2**(win_count-1)

    print(total)