f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]



# part 1

score = 0

for x in range(0,len(lines)):
    baglen = int(len(lines[x])/2)
    bagone = lines[x][:baglen]
    bagtwo = lines[x][baglen:]
    (item,) = set(bagone) & set(bagtwo)
    priority = (ord(item))
    if priority >= 97:
        priority = priority - 96
    else:
        priority = priority - 38
    score = score+priority

print(score)

# part 2

score = 0

for x in range(0,len(lines),3):
    bagone = lines[x]
    bagtwo = lines[x+1]
    bagthree = lines[x+2]
    (item,) = set(bagone) & set(bagtwo) & set(bagthree)
    priority = (ord(item))
    if priority >= 97:
        priority = priority - 96
    else:
        priority = priority - 38
    score = score+priority

print(score)
