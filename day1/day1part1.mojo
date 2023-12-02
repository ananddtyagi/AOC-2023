from python import Python
import time

fn getFirstAndLastDigit(line: String) -> (Int, Int):
    var firstDigitPos: Int = -1
    var lastDigitPos: Int = -1
    for i in range(len(line)):
        if isdigit(ord(line[i])):
            if firstDigitPos == -1:
                firstDigitPos = i
            lastDigitPos = i
        
    return(firstDigitPos, lastDigitPos)

fn main() raises:
    let start = time.now()
    var calibration_sum = 0
    with open("data.txt", "r") as data_file:

        let data = data_file.read()
        var i = 0
        while(i < len(data)):
            let firstDigitPos: Int 
            let lastDigitPos: Int
            var line: String = ""
            while data[i] != '\n' and i != len(data):
                line+=data[i]
                i+=1
            firstDigitPos, lastDigitPos = getFirstAndLastDigit(line)
            calibration_sum += atol(line[firstDigitPos]+line[lastDigitPos])
            i+=1
    print(calibration_sum)
    let end = time.now()
    print((end-start)*1e-9)





