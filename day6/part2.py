with open("data.txt") as data:
    
    lines = data.readlines()
    
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

    time_held = time//2
    ways_to_win = 0
    dist = time_held * (time-time_held)
    
    while(dist > distance):
        ways_to_win += 2
        time_held-=1
        dist = time_held * (time-time_held)

    if time % 2 == 0:
        ways_to_win-=1
    print(ways_to_win)
    
            
        