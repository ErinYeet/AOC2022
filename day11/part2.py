f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

# Parsing

#list of items they have
monkey_items = []
#operation split into a list of values
monkey_ops = []
#the test divide number
monkey_test = []
#targets as True,False
monkey_targets = []

monkey_parse_counter = 0
for x in range(0,len(lines),7):
    x = x + 1
    items = lines[x].split(":")[1].split(",")
    monkey_items.append([int(i) for i in items])
    x = x + 1
    monkey_ops.append(lines[x].split("=")[1].split(" ")[1:])
    x = x + 1
    monkey_test.append(int(lines[x].split(" ")[-1]))
    x = x + 1
    monkey_targets.append([int(lines[x].split(" ")[-1]),int(lines[x+1].split(" ")[-1])])

print(monkey_items)
print(monkey_ops)
print(monkey_test)
print(monkey_targets)

# part 2

monkey_counter = [ 0 for _ in monkey_items]

worry_factor = 1

for n in monkey_test:
    worry_factor = worry_factor * n

for _ in range(10000):
    for m in range(len(monkey_items)):
        while monkey_items[m]:
            item = monkey_items[m].pop(0)
            monkey_counter[m] = monkey_counter[m] + 1
            # Technically the operations cant cover all these possibilities
            # But I want to do this 'properly'
            if monkey_ops[m][0] == 'old':
                a = item
            else:
                a = int(monkey_ops[m][0])
            if monkey_ops[m][2] == 'old':
                b = item
            else:
                b = int(monkey_ops[m][2])
            if monkey_ops[m][1] == '*':
                item = a * b
            else:
                item = a + b

            item = item % worry_factor
            # Throw the item
            test_result = (item % monkey_test[m] == 0)
            if test_result:
                target = monkey_targets[m][0]
            else:
                target = monkey_targets[m][1]
            monkey_items[target].append(item)

monkey_counter.sort()
print(monkey_counter[-1] * monkey_counter[-2])
