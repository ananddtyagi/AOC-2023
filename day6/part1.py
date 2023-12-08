with open("data.txt") as data:
    
    lines = data.readlines()
    
    times = list(map(lambda x: int(x), lines[0].split()[1:]))
    distances = list(map(lambda x: int(x), lines[1].split()[1:]))
    total = 1
    for i, time in enumerate(times):
        time_held = time//2
        ways_to_win = 0
        dist = time_held * (time-time_held)
        
        while(dist > distances[i]):
            ways_to_win += 2
            time_held-=1
            dist = time_held * (time-time_held)

        if time % 2 == 0:
            ways_to_win-=1
        total*=ways_to_win
    print(total)
            
        