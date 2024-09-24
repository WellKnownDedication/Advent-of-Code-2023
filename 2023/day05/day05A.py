if __name__ == "__main__":
    answer = 0

    mappingState = ""

    s2s = []
    with open(r"2023/day05/input") as file:
        for line in file:
            if line != '\n':
                if "seeds:" in line:
                    seedList = line.split()
                elif "seed-to-soil"  in line or mappingState == "seed-to-soil":
                    if mappingState == "":
                        mappingState = "seed-to-soil"
                    else:
                        s2s.append(line.split())
            else:
                mappingState=""
                
    print(seedList)
    print(s2s)

                    
            