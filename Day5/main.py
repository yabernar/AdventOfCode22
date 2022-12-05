import copy

f = open("Day5\input", 'r')
line_count = 0
header_length = 10
number_of_columns = 9
moves = []
stacks = [ [] for _ in range(9) ]
for line in f:
    if line_count < header_length:
        line_count += 1
        if line_count < header_length-1:
            for i in range(number_of_columns):
                if line[1+i*4] != " ":
                    stacks[i].append(line[1+i*4])
    else:
        word = line.rstrip("\n")
        pairs = word.split(" ")
        pairs = [pairs[1], pairs[3], pairs[5]]
        pairs = list(map(int, pairs))
        moves.append(pairs)
f.close()
for lst in stacks:
    lst.reverse()

stacks2 = copy.deepcopy(stacks)

# Part 1

for action in moves:
    for i in range(action[0]):
        stacks[action[2]-1].append(stacks[action[1]-1].pop())

print("Silver: ", end="")
for lst in stacks:
    print(lst[-1], end="")

# Part 2

for action in moves:
    moved = stacks2[action[1]-1][-action[0]:]
    stacks2[action[2]-1] += moved
    stacks2[action[1]-1] = stacks2[action[1]-1][0:-action[0]]

print("\nGold: ", end="")
for lst in stacks2:
    print(lst[-1], end="")