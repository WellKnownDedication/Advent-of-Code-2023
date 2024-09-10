if __name__ == "__main__":
    cardInstances = 0 #answer

    # Inpput example
    # Card   1: 72 28 41 15 98 13 27 99 93 38 | 62  5 80 81 53 29 23 25 59 72 90 19 54 86 68 73 55 21 56 27 32 15 12 42 44
    with open(r"2023/day04/day04B/input") as file:
        lines = [line for line in file]

    cards = []
    cards.append(lines[0])

    for card in cards:
            
        lineNum, line= card.split(':')
        lineNum = lineNum.split()[1]

        winingNums = set(line.split('|')[0].split())
        nums = set(line.split('|')[1].split())

        matches = len(winingNums.intersection(nums))-1

        if matches > 0:
            lb = lines.index(card)
            for i in range(lb, lb + matches):
                cards.append(lines[i])

        cardInstances += 1

    print (cardInstances)