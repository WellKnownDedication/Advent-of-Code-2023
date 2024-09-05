def wordToNum(word):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, n in enumerate(nums):
        if (n in word):
            return i

    return -1