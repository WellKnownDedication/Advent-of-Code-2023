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
            

    for key in mapDict.keys():
        print(key)
        print(mapDict[key])

   
                    
            