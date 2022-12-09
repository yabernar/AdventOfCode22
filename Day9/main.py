f = open("Day9/input", 'r')
movements = []
for line in f:
    move = line.rstrip("\n").split(" ")
    move[1] = int(move[1])
    movements.append(move)
f.close()

# Part 1

head = [0, 0]
tail = [0, 0]
visited_positions = ["0-0"]

def add_pos(pos):
    if pos not in visited_positions:
        visited_positions.append(pos)

def move_rope(x, y, dist):
    for i in range(dist):
        head[0] += x
        head[1] += y
        if abs(head[0]-tail[0]) > 1:
            tail[0] += x
            tail[1] = head[1]
            add_pos(str(tail[0])+"-"+str(tail[1]))
        if abs(head[1]-tail[1]) > 1:
            tail[1] += y
            tail[0] = head[0]
            add_pos(str(tail[0])+"-"+str(tail[1]))

for move in movements:
    if move[0] == "R": move_rope(1, 0, move[1])
    if move[0] == "L": move_rope(-1, 0, move[1])
    if move[0] == "U": move_rope(0, 1, move[1])
    if move[0] == "D": move_rope(0, -1, move[1])

print("Silver:", len(visited_positions))

# Part 2

long_rope = [ [0, 0] for _ in range(10) ]
visited_positions = ["0-0"]

def visualize_rope():
    print_rope = [ ["." for _ in range(6) ] for _ in range(6) ]
    for i in range(len(long_rope)):
        if print_rope[long_rope[i][0]][long_rope[i][1]] == ".":
            print_rope[long_rope[i][0]][long_rope[i][1]] = str(i)
    for i in print_rope:
        for j in i:
            print(j, end=" ")
        print()
    print("---------------")

def move_long_rope(x, y, dist):
    for _ in range(dist):
        long_rope[0][0] += x
        long_rope[0][1] += y
        carrying_on_moving(0)

def carrying_on_moving(knot_nbr):
    if knot_nbr == len(long_rope)-1:
        add_pos(str(long_rope[len(long_rope)-1][0])+"-"+str(long_rope[len(long_rope)-1][1]))
        return
    x_offset = long_rope[knot_nbr][0]-long_rope[knot_nbr+1][0]
    y_offset = long_rope[knot_nbr][1]-long_rope[knot_nbr+1][1]
    if abs(x_offset) > 1 and abs(y_offset) > 1:
        long_rope[knot_nbr+1][0] += int(x_offset/abs(x_offset))
        long_rope[knot_nbr+1][1] += int(y_offset/abs(y_offset))
        carrying_on_moving(knot_nbr+1)
    elif x_offset > 1:
        long_rope[knot_nbr+1][0] += 1
        long_rope[knot_nbr+1][1] = long_rope[knot_nbr][1]
        carrying_on_moving(knot_nbr+1)
    elif x_offset < -1:
        long_rope[knot_nbr+1][0] -= 1
        long_rope[knot_nbr+1][1] = long_rope[knot_nbr][1]
        carrying_on_moving(knot_nbr+1)
    elif y_offset > 1:
        long_rope[knot_nbr+1][1] += 1
        long_rope[knot_nbr+1][0] = long_rope[knot_nbr][0]
        carrying_on_moving(knot_nbr+1)
    elif y_offset < -1:
        long_rope[knot_nbr+1][1] -= 1
        long_rope[knot_nbr+1][0] = long_rope[knot_nbr][0]
        carrying_on_moving(knot_nbr+1)

for move in movements:
    if move[0] == "R": move_long_rope(1, 0, move[1])
    if move[0] == "L": move_long_rope(-1, 0, move[1])
    if move[0] == "U": move_long_rope(0, 1, move[1])
    if move[0] == "D": move_long_rope(0, -1, move[1])

print("Gold:", len(visited_positions))