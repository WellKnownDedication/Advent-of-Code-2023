if __name__ == "__main__":
    answer = 0

    with open(r"day02/day02A/input") as file:
        for game in file:
            requirements = {"red" : 0, "green": 0, "blue": 0}
            fullGame = game.split(":")

            revealList = fullGame[1].split(";")

            for reveal in revealList:
                for cube in reveal.split(","):
                    cubeNumber = int(cube.split(" ")[1])
                    cubeColour = cube.split(" ")[2].rstrip()

                    if (cubeNumber > requirements[cubeColour]):
                        requirements[cubeColour] = cubeNumber
            
            answer = answer + requirements["red"] * requirements[ "green"] * requirements["blue"]
    print(answer)
                

            
                


