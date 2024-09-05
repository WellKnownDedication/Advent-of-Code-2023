import pandas as pd

def wordToNum(word):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, n in enumerate(nums):
        if (n in word):
            return i

    return -1

if __name__ == "__main__":
    total = 0
    data = []

    with open(r"day01/day01B/input") as file:
        for line in file:
            word = ""
            fnum = -1
            lnum = -1
            for char in line:
                if char.isdigit():
                    fnum = char if fnum == -1 else fnum

                    lnum = char
                else:
                    word = word + char
                    
                    num = wordToNum(word)
                    if num > -1:
                        fnum = num if fnum == -1 else fnum

                        lnum = num
                        word = word[-1]

            total = total+ int(str(fnum) + str(lnum))   
            data.append([line, str(fnum) + str(lnum)])
    
    df = pd.DataFrame(data, columns=["line", "value"])
    print (total)

    df.to_excel("day01/day01B/output.xlsx") 
    
