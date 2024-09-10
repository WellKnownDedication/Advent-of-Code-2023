if __name__ == "__main__":
    from queue import Queue
    answer = 0 

    lineMatches = {} # map of cards and their points
    queue = Queue()

    with open(r"2023/day04/input") as file:
        for line in file:
            # Inpput example
            # Card   1: 72 28 41 15 98 13 27 99 93 38 | 62  5 80 81 53 29 23 25 59 72 90 19 54 86 68 73 55 21 56 27 32 15 12 42 44
            lineNum, line = line.split(':')
            lineNum = int(lineNum.split()[1])

            winingNums = set(line.split('|')[0].split())
            nums = set(line.split('|')[1].split())

            points = int(2 ** (len(winingNums.intersection(nums))-1))
            lineMatches[lineNum ] = points # fill map
            queue.put(lineNum)

    while not queue.empty():
        answer += 1

        index = queue.get()
        for i in range(index + 1, index + 1 + lineMatches[index]):
            queue.put(i)

    print (answer)
