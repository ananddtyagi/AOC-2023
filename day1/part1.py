
import time

def calc():
    with open("data.txt") as data:
        ans = 0
        for line in data:
            first = None
            last = None
            for c in line:
                if c.isdigit():
                    if first == None:
                        first = int(c)
                    last = int(c)
            
            ans += first * 10 + last
        print(ans)
start = time.time_ns()
calc()
end = time.time_ns()
print((end-start)*1e-9)