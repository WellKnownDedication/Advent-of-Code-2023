def findNumber(index, rowList):
    left = index
    right = index

    while left-1 > len(rowList) and rowList[left-1].isnumeric():
        left -= 1

    while right+1 > len(rowList) and rowList[right+1].isnumeric():
        right += 1

    number = ""
    for i in range(left, right):
        number += list[i]
    
    if number == "":
        return (left, right, 0)

    return (left, right, int(number))


if __name__ == "__main__":
    answer = 0

    symbols = []
    lineList = []

    with open(r"day03/day03A/input") as file:
        for line in file:
            lineList.append(list(line))

            for symbol in list(line):
                if not symbol.isnumeric() and symbol != "." and symbol not in symbols:
                    symbols.append(symbol)

    del file
    del line

    for y in range(0, len(lineList)):
        for x in range(0, len(lineList[y])):
            if lineList[y][x] in symbols:
                
                if y > 0 : minI = y-1 
                else: minI = y 

                if y < len(lineList) : maxI = y+1 
                else: maxI = y

                if x > 0 : minJ = x-1 
                else: minJ = x 

                if x < len(lineList) : maxJ = x+1 
                else: maxJ = x

                # search around point
                for i in range(minI, maxI):
                    for j in range (minJ, maxJ):
                        if i != y and j != x:
                            holder = findNumber(x, lineList[i])

                            answer += holder[2]
                            j = holder[1]

    print(answer)

                


