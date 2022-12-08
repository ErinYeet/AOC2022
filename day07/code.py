from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace('\n','') for line in lines]

# part 1

pwd = []

# files represented with path as key, size as value
files = {}

# dirs represented with path as key, subcontents as value
dirs = defaultdict(list)


for x in range(0,len(lines)):
    line = lines[x]
    if line == "$ cd /":
        pwd = [""]
    elif line == "$ cd ..":
        pwd.pop()
    elif line[0:5] == "$ cd ":
        pwd.append(line[5:])
    elif line == "$ ls":
        x = x+1
        while x < len(lines):
            line = lines[x]
            if line[0] == "$":
                break
            if line[0:3] == "dir":
                dirs["/".join(pwd)].append(line[4:])
            else:
                files["/".join(pwd)+"/"+line.split()[1]] = int(line.split()[0])
                dirs["/".join(pwd)].append(line.split()[1])
            x = x+1

dirsizes = {}

for key,value in dirs.items():
    dirsizes[key] = 0

for key in files:
    # add the size of the file to all of its parent directories
    pathlist = key.split('/')
    pathlist.pop()
    while pathlist:
        dirsizes['/'.join(pathlist)] = dirsizes['/'.join(pathlist)] + files[key]
        pathlist.pop()


answer = 0

for k in dirsizes:
    if dirsizes[k] <= 100000:
        answer = answer + dirsizes[k]
print(answer)

# part 2

disksize = 70000000
required = 30000000
needtogain = required - (disksize - dirsizes[""])
print(needtogain)
smallest = 70000000

for k in dirsizes:
    if dirsizes[k] < smallest and dirsizes[k] > needtogain:
        smallest = dirsizes[k]
print(smallest)


