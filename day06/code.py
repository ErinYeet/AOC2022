f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace('\n','') for line in lines]

# part 1

line = lines[0]

for x in range(4,len(line)):
    marker = line[x-4:x]
    if len(set(marker))==4:
        break

print(x)

# part 2

for x in range(14,len(line)):
    marker = line[x-14:x]
    if len(set(marker))==14:
        break

print(x)
