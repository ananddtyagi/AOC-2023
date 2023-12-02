with open("data.txt") as data:
    games = 0
    for line in data:
        red = 12
        green = 13
        blue = 14
        
        color_map = {"green": -1, "red": -1, "blue": -1}
        
        game, game_info = line.strip().split(": ")
        states = game_info.split("; ")
        for state in states:
            showed = state.split(", ")
            for shown in showed:
                count, color = shown.split(" ")
                # if color_map[color] == -1:
                #     color_map[color] = int(count)
                # else:
                color_map[color] = max( color_map[color] , int(count))
        x = 1
        for val in color_map.values():
            x *= val
        # print(x)
        games += x
    print(games)

            
        