def tos(elf):
    return str(elf[0])+","+str(elf[1])

def tol(elf):
    return list(map(int, elf.split(",")))

f = open("Day23/input", 'r')
elves = {}
y = 0
for line in f:
    line = line.strip("\n")
    for x in range(len(line)):
        if line[x] == "#":
            elves[tos([x, y])] = [x,y]
    y += 1
f.close()

# Part 1
cardinals = ["N", "S", "W", "E"]

def look_around(elf):
    neighbors = set()
    if tos([elf[0]-1, elf[1]-1]) in elves or tos([elf[0], elf[1]-1]) in elves or tos([elf[0]+1, elf[1]-1]) in elves: neighbors.add("N")
    if tos([elf[0]-1, elf[1]+1]) in elves or tos([elf[0], elf[1]+1]) in elves or tos([elf[0]+1, elf[1]+1]) in elves: neighbors.add("S")
    if tos([elf[0]+1, elf[1]-1]) in elves or tos([elf[0]+1, elf[1]]) in elves or tos([elf[0]+1, elf[1]+1]) in elves: neighbors.add("E")
    if tos([elf[0]-1, elf[1]-1]) in elves or tos([elf[0]-1, elf[1]]) in elves or tos([elf[0]-1, elf[1]+1]) in elves: neighbors.add("W")
    return neighbors

def move_elf(elf, direction):
    if direction == "N": return [elf[0], elf[1]-1]
    if direction == "S": return [elf[0], elf[1]+1]
    if direction == "E": return [elf[0]+1, elf[1]]
    if direction == "W": return [elf[0]-1, elf[1]]

def round():
    next_moves = {}
    forbidden_moves = set()
    for elf in elves:
        neighbors = look_around(elves[elf])
        if neighbors:
            for direction in cardinals:
                if direction not in neighbors:
                    move = tos(move_elf(elves[elf], direction))
                    if move not in forbidden_moves:
                        if move not in next_moves:
                            next_moves[move] = elf
                        else:
                            forbidden_moves.add(move)
                            next_moves.pop(move)
                    break
    for k, v in next_moves.items():
        elves[k] = tol(k)
        elves.pop(v)
    cardinals.append(cardinals.pop(0))
    return len(next_moves) != 0

def find_rectangle():
    lx, ly = [], []
    for e in elves.values():
        lx.append(e[0])
        ly.append(e[1])
    return (max(lx)+1-min(lx)) * (max(ly)+1-min(ly)) - len(elves)

def show_elves():
    lx, ly = [], []
    for e in elves:
        lx.append(elves[e][0])
        ly.append(elves[e][1])
    for y in range(min(ly), max(ly)+1):
        for x in range(min(lx), max(lx)+1):
            if tos([x, y]) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()


for i in range(10):round()
print("Silver:", find_rectangle())
#show_elves()

k = 11
while round(): k += 1
print("Gold:", k)
