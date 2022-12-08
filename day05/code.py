f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace('\n','') for line in lines]

# part 1

numpiles = int((len(lines[0])+1)/4)

piles = [[] for _ in range(numpiles)]
print(piles)

for x in range(0,len(lines)):
    line = lines[x]
    if line[1] == '1':
        break
    for n in range(numpiles):
        if line[n*4+1] != ' ':
            piles[n].append(line[n*4+1])
print(x)
print(piles)

[pile.reverse() for pile in piles]
print(piles)

instart = x+2

for x in range(instart,len(lines)):
    line = lines[x]
    linelist = line.split()
    amount = int(linelist[1])
    source = int(linelist[3])-1
    dest = int(linelist[5])-1
    for n in range(amount):
        piles[dest].append(piles[source].pop())
print(piles)

output = []

for pile in piles:
    output.append(pile[-1])

print("".join(output))

# part 2

numpiles = int((len(lines[0])+1)/4)

piles = [[] for _ in range(numpiles)]
print(piles)

for x in range(0,len(lines)):
    line = lines[x]
    if line[1] == '1':
        break
    for n in range(numpiles):
        if line[n*4+1] != ' ':
            piles[n].append(line[n*4+1])
print(x)
print(piles)

[pile.reverse() for pile in piles]
print(piles)

instart = x+2

for x in range(instart,len(lines)):
    line = lines[x]
    linelist = line.split()
    amount = int(linelist[1])
    source = int(linelist[3])-1
    dest = int(linelist[5])-1
    crane = piles[source][(-1*amount):]
    piles[dest].extend(crane)
    del piles[source][(-1*amount):]
print(piles)

output = []

for pile in piles:
    output.append(pile[-1])

print("".join(output))
