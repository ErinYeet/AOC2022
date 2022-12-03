f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

elfcalories = []
curcal = 0

for x in range(1,len(lines)):
    if lines[x] == '':
        elfcalories.append(curcal)
        curcal = 0
    else:
        curcal = curcal + int(lines[x])

# Part 1
print(max(elfcalories))

# Part 2
elfcalories.sort()
elfcalories.reverse()
print(sum(elfcalories[0:3]))
