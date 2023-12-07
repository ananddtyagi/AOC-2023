


def max(a: Int ,b: Int) -> Int:
    if a>b: return a else: return b
fn main() raises:
    with open("data.txt", "r") as f:
        let data = f.read()
        var games = 0

        var line_n = 0
        let lines = data.split("\n")
        while (line_n < lines.size):
            var g = -1
            var r = -1
            var b = -1
            let line_info = lines[line_n].split(": ")
            
            let states = line_info[1].split("; ")
            for i in range(states.size):
                let showed = states[i].split(", ")
                for j in range(showed.size):
                    let showed_info = showed[j].split(" ")
                    if showed_info[1] == "green":
                        g = max(g, atol(showed_info[0]))
                    if showed_info[1] == "red":
                        r = max(r, atol(showed_info[0]))
                    if showed_info[1] == "blue":
                        b = max(b, atol(showed_info[0]))

            games += g*r*b
            line_n+=1
        print(games)