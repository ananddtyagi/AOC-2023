with open("data.txt") as data:
    games = 0
    for line in data:
        color_map = {"green": 13, "red": 12, "blue": 14}
        
        game, game_info = line.strip().split(": ")
        states = game_info.split("; ")
        passed = True
        for state in states:
            showed = state.split(", ")
            for shown in showed:
                count, color = shown.split(" ")
                if color_map[color] < int(count):
                    passed = False
        if passed:
            games += int(game.split(" ")[1])
    print(games)

            
        