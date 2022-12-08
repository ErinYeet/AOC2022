f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

# part 1

score = 0

for x in range(0,len(lines)):
    line = lines[x].replace(",","-")
    numbers = line.split("-")
    if (int(numbers[0]) >= int(numbers[2]) and int(numbers[1]) <= int(numbers[3])) or (int(numbers[0]) <= int(numbers[2]) and int(numbers[1]) >= int(numbers[3])):
        score = score + 1
    

print(score)

# part 2

score = 0

for x in range(0,len(lines)):
    line = lines[x].replace(",","-")
    numbers = line.split("-")
    #by the powers of maths there must be a much better way but i tried to find it and I got the wrong answer
    if (int(numbers[0]) >= int(numbers[2]) and int(numbers[0]) <= int(numbers[3])) or (int(numbers[1]) >= int(numbers[2]) and int(numbers[1]) <= int(numbers[3])) or (int(numbers[2]) >= int(numbers[0]) and int(numbers[2]) <= int(numbers[1])) or (int(numbers[3]) >= int(numbers[0]) and int(numbers[3]) <= int(numbers[1])):
        score = score + 1
    

print(score)
