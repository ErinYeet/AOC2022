f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

# part 1

score = 0
checkcycles = [20,60,100,140,180,220]
cycles = 0
position = 0
register = 1


while True:
    cycles = cycles + 1
    if cycles in checkcycles:
        score = score + register*cycles
    if lines[position % len(lines)][0] == "a":
        cycles = cycles + 1
        if cycles in checkcycles:
            score = score + register*cycles
        register = register + int(lines[position % len(lines)].split(" ")[1])
    position = position + 1
    if cycles > 220:
        break


print(score)

# part 2

cycles = 0
position = 0
register = 1

toprint = [[] for n in range(6)]

while True:
    cycles = cycles + 1
    if abs(((cycles-1) % 40) - register) <= 1 :
        toprint[(cycles-1)//40].append('#')
    else:
        toprint[(cycles-1)//40].append('.')
    if lines[position % len(lines)][0] == "a":
        cycles = cycles + 1
        if abs(((cycles-1) % 40) - register) <= 1 :
            toprint[(cycles-1)//40].append('#')
        else:
            toprint[(cycles-1)//40].append('.')
        register = register + int(lines[position % len(lines)].split(" ")[1])
    position = position + 1
    if cycles >= 240:
        break
    print(cycles,register)
    print("\n".join(["".join(printline) for printline in toprint]))
