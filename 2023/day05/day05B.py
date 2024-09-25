if __name__ == "__main__":
    answer = 0

    mappingState = ""
    mapDict = {"seed-to-soil":[], 
               "soil-to-fertilizer":[], 
               "fertilizer-to-water": [], 
               "water-to-light": [], 
               "light-to-temperature":[],
               "temperature-to-humidity":[],
               "humidity-to-location":[]}
    
    with open(r"2023/day05/input") as file:
        for line in file:
            if "seeds:" in line:
                seeds = line.split(":")[1].split()
            elif mappingState == "" and "map:" in line:
                mappingState = line.split()[0]
            elif mappingState != "" and line != "\n":
                mapDict[mappingState].append(line.split())
            else:
                mappingState = ""
    
    seedBuffer = 0
    actualSeeds = []
    for i in range(0,len(seeds)):
        if i % 2 == 0: # is range of seeds
            for j in range(seedBuffer, seedBuffer + int(seeds[i])):
                actualSeeds.append(seedBuffer+j)
        else: # is seed
            seedBuffer = int(seeds[i])
            actualSeeds.append(seedBuffer)

    seedsMapped = []
    for seed in actualSeeds:                  # for each seed
        mapping = seed
        for mapKey in mapDict.keys():   # for each map in mapDict(seed-to-soil, soild-to-fertilizer,...)
            mappingList = mapDict[mapKey]

            for m in mappingList:
                sourceR = m[1]  # in seed-to-soil this is seed
                destR = m[0]    # in seed-to-soil this is soil
                R = m[2]        # range

                if mapping >= sourceR and mapping < sourceR + R:
                    mapping = destR + (mapping - sourceR)
                    break
        
        if answer == 0 or answer > mapping:
            answer = mapping

    print(answer)


    
