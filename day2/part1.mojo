fn main() raises:
    with open("data.txt", "r") as f:
        let data = f.read()
        var games = 0
        let red = 12
        let green = 13
        let blue = 14

        var line_n = 0
        let lines = data.split("\n")
        while (line_n < lines.size):
            let line_info = lines[line_n].split(": ")
            
            let states = line_info[1].split("; ")
            var passed = True
            for i in range(states.size):
                let showed = states[i].split(", ")
                for j in range(showed.size):
                    let showed_info = showed[j].split(" ")
                    if showed_info[1] == "green" and green < atol(showed_info[0]):
                        passed = False
                    if showed_info[1] == "red" and red < atol(showed_info[0]):
                        passed = False
                    if showed_info[1] == "blue" and blue < atol(showed_info[0]):
                        passed = False
            if passed:
                games += atol(line_info[0].split(" ")[1])
            line_n+=1
        print(games)