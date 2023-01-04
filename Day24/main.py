import math
import copy

f = open("Day24/input", 'r')
valley = []
for line in f:
    line = line.strip("#\n")
    if line != ".":
        line = list(line)
        winds = []
        for i in line:
            if i == ".":
                winds.append([])
            else:
                winds.append([i])
        valley.append(winds)
f.close()

# Part 1
width = len(valley[0])
height = len(valley)

def tos(elf):
    return str(elf[0])+","+str(elf[1])

def tol(elf):
    return list(map(int, elf.split(",")))

def show_winds(winds):
    for y in range(height):
        for x in range(width):
            if len(winds[y][x]) == 1:
                print(winds[y][x][0], end="")
            else:
                print(len(winds[y][x]), end="")
        print()
    print("-------------")

def winds_howling(old):
    new = [[[] for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            for w in old[y][x]:
                if w == ">": new[y][(x+1)%width].append(">")
                elif w == "<": new[y][(x-1+width)%width].append("<")
                elif w == "v": new[(y+1)%height][x].append("v")
                elif w == "^": new[(y-1+height)%height][x].append("^")
    return new

finished = False
back_for_snacks = False
snacks_in_pocket = False
time = 0
silver = 0
positions = set()

while not finished:
    valley = winds_howling(valley)
    time += 1
    new_positions = set()
    for pos in positions:
        p = tol(pos)
        if valley[p[0]][p[1]] == []: new_positions.add(pos) # Wait
        if p[0] > 0 and valley[p[0]-1][p[1]] == []: new_positions.add(tos([p[0]-1, p[1]]))
        if p[0] < height-1 and valley[p[0]+1][p[1]] == []: new_positions.add(tos([p[0]+1, p[1]]))
        if p[1] > 0 and valley[p[0]][p[1]-1] == []: new_positions.add(tos([p[0], p[1]-1]))
        if p[1] < width-1 and valley[p[0]][p[1]+1] == []: new_positions.add(tos([p[0], p[1]+1]))
    if (snacks_in_pocket or not back_for_snacks) and valley[0][0] == []: new_positions.add("0,0") # Spawn top left
    if (back_for_snacks and not snacks_in_pocket) and valley[height-1][width-1] == []: new_positions.add(tos([height-1, width-1])) # Spawn bottom right
    positions = new_positions
    if tos([height-1, width-1]) in positions and snacks_in_pocket: finished = True
    if tos([height-1, width-1]) in positions and not back_for_snacks: 
        back_for_snacks = True
        valley = winds_howling(valley)
        time += 1
        silver = time
        positions = set()
    if tos([0, 0]) in positions and back_for_snacks and not snacks_in_pocket:
        snacks_in_pocket = True
        valley = winds_howling(valley)
        time += 1
        positions = set()

print("Silver:", silver)
print("Gold:", time+1)