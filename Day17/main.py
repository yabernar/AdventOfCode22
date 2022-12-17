f = open("Day17/input", 'r')
jet_patterns = ""
for line in f:
    jet_patterns = line.rstrip("\n")
f.close()

def place_rock(positions_list):
    for p in positions_list:
        tower[p[0]][p[1]] = "#"

def collision(positions_list):
    for p in positions_list:
        if p[0]<0 or p[1]<0 or p[1]>6: return True
        if tower[p[0]][p[1]] == "#": return True

def shape_line(pos):
    shape_pos = []
    for k in range(4):
        shape_pos.append([pos[0], pos[1]+k])
    return shape_pos

def shape_cross(pos):
    shape_pos = [[pos[0], pos[1]], 
                [pos[0]+1, pos[1]-1], 
                [pos[0]+1, pos[1]], 
                [pos[0]+1, pos[1]+1], 
                [pos[0]+2, pos[1]]]
    return shape_pos

def shape_L(pos):
    shape_pos = [[pos[0], pos[1]], 
                [pos[0], pos[1]+1], 
                [pos[0], pos[1]+2], 
                [pos[0]+1, pos[1]+2], 
                [pos[0]+2, pos[1]+2]]
    return shape_pos

def shape_vertical(pos):
    shape_pos = []
    for k in range(4):
        shape_pos.append([pos[0]+k, pos[1]])
    return shape_pos

def shape_square(pos):
    shape_pos = [[pos[0], pos[1]], 
                 [pos[0], pos[1]+1], 
                 [pos[0]+1, pos[1]], 
                 [pos[0]+1, pos[1]+1]]
    return shape_pos

line = {"left":0, "right":4, "top":1, "shape":shape_line}
cross = {"left":1, "right":1, "top":3, "shape":shape_cross}
lshape = {"left":0, "right":2, "top":3, "shape":shape_L}
vertical = {"left":0, "right":0, "top":4, "shape":shape_vertical}
square = {"left":0, "right":1, "top":2, "shape":shape_square}

def print_tower(height):
    for i in range(height, height-11,-1):
        for j in tower[i]:
            print(j, end="")
        print()
    print("+------+")

def same_shape(height, height2):
    for i in range(20):
        for j in range(7):
            if tower[height-i-1][j] != tower[height2-i-1][j]:
                return False
    return True

def jet_wash(position, rock_type, jet_cursor):
    if jet_patterns[jet_cursor] == "<":
        if not collision(rock_type["shape"]([position[0], position[1]-1])):
            position[1] -= 1
    else:
        if not collision(rock_type["shape"]([position[0], position[1]+1])):
            position[1] += 1
    return position

def tetris(nb_rocks):
    loops = {}
    types = [line, cross, lshape, vertical, square]
    jet_cursor = 0
    highest_rock = 0
    height_per_loop = 0
    number_of_loops = 0
    looped = False
    i = 0

    while i < nb_rocks:
        rock_type = types[i%len(types)]
        position = [highest_rock+3, 2+rock_type["left"]]
        if not looped:
            if jet_cursor in loops:
                if types.index(rock_type) in loops[jet_cursor]:
                    for p in loops[jet_cursor][types.index(rock_type)]:
                        if same_shape(highest_rock, p[0]):
                            height_before_cycle = highest_rock
                            number_of_loops = (nb_rocks-i-1)//(i - p[1])
                            height_per_loop = highest_rock - p[0]
                            i += number_of_loops*(i - p[1])
                            looped = True
                            break
                    if not looped:
                        loops[jet_cursor][types.index(rock_type)].append([highest_rock, i])
                else:
                    loops[jet_cursor][types.index(rock_type)] = [[highest_rock, i]]
            else:
                loops[jet_cursor] = {types.index(rock_type): [[highest_rock, i]]}
        stop = False
        while not stop:
            position = jet_wash(position, rock_type, jet_cursor)
            jet_cursor = (jet_cursor+1) % len(jet_patterns)
            position[0] -= 1
            if position[0] < highest_rock:
                shape_if_moved = rock_type["shape"](position)
                if collision(shape_if_moved):
                    position[0] += 1
                    place_rock(rock_type["shape"](position))
                    highest_rock = max(highest_rock, position[0]+rock_type["top"])
                    stop = True
        i += 1
    return highest_rock+height_per_loop*number_of_loops

tower = [["."] * 7 for _ in range(100000)]
print("Silver:", tetris(2022))
tower = [["."] * 7 for _ in range(100000)]
print("Gold:", tetris(1000000000000))