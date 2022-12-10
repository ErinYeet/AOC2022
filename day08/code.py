from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace('\n','') for line in lines]

# part 1

visible = 0
grid = []

for line in lines:
    intline = [int(x) for x in line]
    grid.append(intline)

print(grid)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == 0 or (x == (len(grid[y])-1)) or y == 0 or (y == (len(grid)-1)):
            visible = visible + 1
        else:
            north = [grid[n][x] for n in range(0,y)]
            if max(north) < grid[y][x]:
                visible = visible + 1
                continue
            south = [grid[n][x] for n in range(y+1,len(grid[y]))]
            if max(south) < grid[y][x]:
                visible = visible + 1
                continue
            west = grid[y][:x]
            if max(west) < grid[y][x]:
                visible = visible + 1
                continue
            east = grid[y][x+1:]
            if max(east) < grid[y][x]:
                visible = visible + 1
                continue
        
print(visible)

# part 2

maxb = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == 0 or (x == (len(grid[y])-1)) or y == 0 or (y == (len(grid)-1)):
            continue
        north = 0
        for n in range(y-1,-1,-1):
            north = north + 1
            if grid[n][x] >= grid[y][x]:
                break
        south = 0
        for n in range(y+1,len(grid),1):
            south = south + 1
            if grid[n][x] >= grid[y][x]:
                break
        west = 0
        for n in range(x-1,-1,-1):
            west = west + 1
            if grid[y][n] >= grid[y][x]:
                break
        east = 0
        for n in range(x+1,len(grid[y]),1):
            east = east + 1
            if grid[y][n] >= grid[y][x]:
                break
        beauty = (north * south * west * east)
        #print(x,y)
        #print(north,south,east,west, beauty)
        if beauty > maxb:
            maxb = beauty
            
print(maxb)
