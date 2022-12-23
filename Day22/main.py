import re
import copy
import numpy as np

f = open("Day22/input", 'r')
carte = []
instructions = ""
instruction_line = False
for line in f:
    line = line.strip("\n")
    if line == "":
        instruction_line = True
    elif instruction_line:
        instructions = line
    else:
        carte.append(list(line))
f.close()
instructions = re.split("(R|L)", instructions)

# Part 1

visited = copy.deepcopy(carte)
for i in range(len(visited)):
    visited[i] = list(visited[i])
    carte[i] = carte[i] + [" " for _ in range(200 - len(carte[i]))]
    
orientations = {0: (1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}

def show_map(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="")
        print()

def move(x, y, d_x, d_y, dist):
    for i in range(dist):
        k = 1
        n_x = (x + d_x + len(carte[0])) % len(carte[0])
        n_y = (y + d_y + len(carte)) % len(carte)
        while carte[n_y][n_x] == " ":
            k += 1
            n_x = (x + d_x*k + len(carte[0])) % len(carte[0])
            n_y = (y + d_y*k + len(carte)) % len(carte)
        if carte[n_y][n_x] == ".":
            x, y = n_x, n_y
            #visited[y][x] = "@"
        elif carte[n_y][n_x] == "#":
            return x, y
    return x, y

ori = 0
x, y = move(0, 0, orientations[ori][0], orientations[ori][1], 1)

for inst in instructions:
    if inst == "R":
        ori = (ori+1)%4
    elif inst == "L":
        ori = (ori+4-1)%4
    else:
        x, y = move(x, y, orientations[ori][0], orientations[ori][1], int(inst))
print("Silver:", 1000*(y+1)+4*(x+1)+ori)

# Part 2
cube_size = 50
# shape = ["--A", "DEB", "--CF"]
# cube_map = {}
# for i in range(len(shape)):
#     for j in range(len(shape[i])):
#         if shape[i][j] != "-":
#             line = carte[i*cube_size:(i+1)*cube_size]
#             for k in range(len(line)):
#                 line[k] = list(line[k][j*cube_size:(j+1)*cube_size])
#             cube_map[shape[i][j]] = line
# print(cube_map)

def move_cube(x, y, ori, dist):
    for i in range(dist):
        visited[y-1][x-1] = "@"
        n_x = x + orientations[ori][0]
        n_y = y + orientations[ori][1]
        n_ori = ori
        if isinstance(cube_map[n_y][n_x], list):
            ncd = cube_map[n_y][n_x]
            n_x = ncd[0]
            n_y = ncd[1]
            n_ori = ncd[2]
        if isinstance(cube_map[n_y][n_x], dict):
            ncd = cube_map[n_y][n_x][ori]
            n_x = ncd[0]
            n_y = ncd[1]
            n_ori = ncd[2]      
        if cube_map[n_y][n_x] == ".":
            x, y, ori = n_x, n_y, n_ori
        elif cube_map[n_y][n_x] == "#":
            return x, y, ori
    visited[y-1][x-1] = "@"
    return x, y, ori

cube_map = copy.deepcopy(carte)
for l in cube_map:
    l.insert(0, "+")
cube_map.insert(0, list("+" * len(cube_map[0])))
cube_map.append(list("+" * len(cube_map[len(cube_map)-1])))

# 6 and 4
cube_map[cube_size+1][cube_size*2+1] = {0:[cube_size*2+1, cube_size, 3], 1:[cube_size*2, cube_size+1, 2]}
for i in range(1, cube_size):
    cube_map[cube_size+1][cube_size*2+i+1] = [cube_size*2, cube_size+i+1, 2]
    cube_map[cube_size+i+1][cube_size*2+1] = [cube_size*2+i+1, cube_size-1+1, 3]
# 2 and 5
cube_map[cube_size*3+1][cube_size+1] = {0:[cube_size+1, cube_size*3, 3], 1:[cube_size, cube_size*3+1, 2]}
for i in range(1, cube_size):
    cube_map[cube_size*3+1][cube_size+i+1] = [cube_size, cube_size*3+i+1, 2]
    cube_map[cube_size*3+i+1][cube_size+1] = [cube_size+i+1, cube_size*3-1+1, 3]
# 3 and 4
cube_map[cube_size*2][cube_size] = {2:[cube_size, cube_size*2+1, 1], 3:[cube_size+1, cube_size*2, 0]}
for i in range(1, cube_size):
    cube_map[cube_size*2][cube_size-i] = [cube_size+1, cube_size*2-i, 0]
    cube_map[cube_size*2-i][cube_size] = [cube_size-i, cube_size*2+1, 1]
# 1 and 3
for i in range(1, cube_size+1):
    cube_map[i][cube_size] = [1, cube_size*3-i+1, 0]
    cube_map[cube_size*3-i+1][0] = [cube_size+1, i, 0]
# 1 and 2
for i in range(1, cube_size+1):
    cube_map[0][cube_size+i] = [1, cube_size*3+i, 0]
    cube_map[cube_size*3+i][0] = [cube_size+i, 1, 1]
# 5 and 6
for i in range(1, cube_size+1):
    cube_map[i][cube_size*3+1] = [cube_size*2, cube_size*3-i+1, 2]
    cube_map[cube_size*3-i+1][cube_size*2+1] = [cube_size*3, i, 2]
# 6 and 2
for i in range(1, cube_size+1):
    cube_map[0][cube_size*2+i] = [i, cube_size*4, 3]
    cube_map[cube_size*4+1][i] = [cube_size*2+i, 1, 1]

#show_map(cube_map)

x, y, ori = 51, 1, 0
for inst in instructions:
    if inst == "R":
        ori = (ori+1)%4
    elif inst == "L":
        ori = (ori+4-1)%4
    else:
        x, y, ori = move_cube(x, y, ori, int(inst))
print("Gold:", 1000*y+4*x+ori)
#print(x, y, ori)
#show_map(visited)
