f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

# part 1

# y,x pos y is down
head = [0,0]
tail = [0,0]
# maps coords as string to True when touched by tail
touched = {"0,0":True}

for line in lines:
    direction = line.split(" ")[0]
    dist = int(line.split(" ")[1])
    if direction == "U":
        head[0] = head[0] - dist
    if direction == "D":
        head[0] = head[0] + dist
    if direction == "R":
        head[1] = head[1] + dist
    if direction == "L":
        head[1] = head[1] - dist
    while abs(head[0]-tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        if tail[0] < head[0]:
            tail[0] = tail[0] + 1
        elif tail[0] > head[0]:
            tail[0] = tail[0] - 1
        if tail[1] < head[1]:
            tail[1] = tail[1] + 1
        elif tail[1] > head[1]:
            tail[1] = tail[1] - 1
        touched[",".join([str(x) for x in tail])] = True
print(len(touched))

# part 2, I could have rewritten part 1 to use this format but this feels more honest

rope = [ [0,0] for _ in range(10)]
touched_two = {"0,0":True}

for line in lines:
    direction = line.split(" ")[0]
    dist = int(line.split(" ")[1])
    for n in range(dist):
        if direction == "U":
            rope[0][0] = rope[0][0] - 1
        if direction == "D":
            rope[0][0] = rope[0][0] + 1
        if direction == "R":
            rope[0][1] = rope[0][1] + 1
        if direction == "L":
            rope[0][1] = rope[0][1] - 1
        for x in range(1,10):
            if abs(rope[x-1][0]-rope[x][0]) <= 1 and abs(rope[x-1][1] - rope[x][1]) <= 1:
                continue
            if rope[x][0] < rope[x-1][0]:
                rope[x][0] = rope[x][0] + 1
            elif rope[x][0] > rope[x-1][0]:
                rope[x][0] = rope[x][0] - 1
            if rope[x][1] < rope[x-1][1]:
                rope[x][1] = rope[x][1] + 1
            elif rope[x][1] > rope[x-1][1]:
                rope[x][1] = rope[x][1] - 1
            if x == 9:
                touched_two[",".join([str(x) for x in rope[x]])] = True
print(len(touched_two))
