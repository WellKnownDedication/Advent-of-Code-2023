if __name__ == "__main__":
    sum = 0

    with open(r"day01/day01A\input") as file:
        for line in file:
            fnum = -1
            lnum = -1
            for char in line:
                if char.isdigit():
                    fnum = char if fnum == -1 else fnum

                    lnum = char
            
            sum = sum + int(str(fnum) + str(lnum))
    
    print (sum)
