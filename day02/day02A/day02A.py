if __name__ == "__main__":
    requirements = {"red" : 12, "green": 13, "blue": 14}
    answer = 0

    with open(r"day02/day02A/input") as file:
        for game in file:
            gamePossible = True
            fullGame = game.split(":")

            gameID = int(fullGame[0].split(" ")[1])
            revealList = fullGame[1].split(";")

            for reveal in revealList:
                for cube in reveal.split(","):
                    cubeNumber = int(cube.split(" ")[1])
                    cubeColour = cube.split(" ")[2].rstrip()

                    if (requirements.get(cubeColour) == None):
                        gamePossible = False
                    elif (cubeNumber > requirements.get(cubeColour)):
                        gamePossible = False

            if (gamePossible): 
                answer  += gameID

    print(answer)
                

            
                


