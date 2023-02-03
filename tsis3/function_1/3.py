def solve(numheads, numlegs):
    return int((numlegs-2*numheads)/2), int(numheads-(numlegs-2*numheads)/2)


numheads,numlegs = map(int, input().split())


print("Rabbits number: ", solve(numheads, numlegs)[0], "\nChickens number: ", solve(numheads, numlegs)[1])
