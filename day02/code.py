f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

# Part 1
score = 0
for x in range(0,len(lines)):
    if lines[x][2] == 'X':
        score = score + 1
        if lines[x][0] == 'A':
            score = score + 3
        elif lines[x][0] == 'B':
            score = score + 0
        elif lines[x][0] == 'C':
            score = score + 6
    elif lines[x][2] == 'Y':
        score = score + 2
        if lines[x][0] == 'A':
            score = score + 6
        elif lines[x][0] == 'B':
            score = score + 3
        elif lines[x][0] == 'C':
            score = score + 0
    elif lines[x][2] == 'Z':
        score = score + 3
        if lines[x][0] == 'A':
            score = score + 0
        elif lines[x][0] == 'B':
            score = score + 6
        elif lines[x][0] == 'C':
            score = score + 3

print(score)

# Part 2
score = 0
for x in range(0,len(lines)):
    if lines[x][2] == 'X':
        if lines[x][0] == 'A':
            score = score + 3
        elif lines[x][0] == 'B':
            score = score + 1
        elif lines[x][0] == 'C':
            score = score + 2
    elif lines[x][2] == 'Y':
        if lines[x][0] == 'A':
            score = score + 4
        elif lines[x][0] == 'B':
            score = score + 5
        elif lines[x][0] == 'C':
            score = score + 6
    elif lines[x][2] == 'Z':
        if lines[x][0] == 'A':
            score = score + 8
        elif lines[x][0] == 'B':
            score = score + 9
        elif lines[x][0] == 'C':
            score = score + 7

print(score)
