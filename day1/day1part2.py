import time

def getDigits(s: str):
    spelled_digits = {'o': ['one'],
                      't': ['two', 'three'],
                      'f': ['four', 'five'],
                      's': ['six', 'seven'],
                      'e': ['eight'],
                      'n': ['nine']
                      }
    spelling_to_value = {'one': 1,
                         'two': 2,
                         'three': 3,
                         'four': 4,
                         'five': 5,
                         'six': 6,
                         'seven': 7,
                         'eight': 8,
                         'nine': 9
                         }
    
    first = None
    last = None
    i = 0
    
    while i < len(s):
        c = s[i]
        digit = None
        if c.isdigit():
            digit = int(c)
            i+=1
        else:
            if c in spelled_digits:
                potential_digits = spelled_digits[c]
                for p in potential_digits:
                    if s[i:i+len(p)] == p:
                        digit = spelling_to_value[p]
                        i += 1
                        break
        if digit == None:
            i+=1
        else:
            if first == None:
                first = digit
            last = digit
    
    return first, last
                
def calc():
    with open("data.txt") as data:
        ans = 0
        for line in data:
            first, last = getDigits(line.strip())
            print(line, first, last)
            ans += first * 10 + last
        print(ans)
start = time.time_ns()
calc()
end = time.time_ns()
print((end-start)*1e-9)