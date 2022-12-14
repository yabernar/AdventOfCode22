f = open("Day14/input", 'r')
rocks = []
MAX = 99999999999
min_x, max_x = MAX, -1
min_y, max_y = MAX, -1
for line in f:
    row = line.rstrip("\n").split(" -> ")
    path = []
    for pos in row:
        p = pos.split(",")
        x, y = int(p[0]), int(p[1])
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)
        path.append([x, y])
    rocks.append(path)
f.close()

# Part 1

scan = [["." for _ in range(0, max_y+2)] for _ in range(1000)]

def show_map():
    for y in range(len(scan[0])):
        for x in range(len(scan)):
            print(scan[x][y], end="")
        print()

def count_stillsand():
    count = 0
    for i in scan:
        for j in i:
            if j == "o": count += 1
    return count

def add_rock_formations():
    for path in rocks:
        for point in range(len(path)-1):
            if path[point][0] == path[point+1][0]: # Vertical
                one, two = path[point][1], path[point+1][1]
                for i in range(min(one, two), max(one, two)+1):
                    scan[path[point][0]][i] = "#"
            else: # Horizontal
                one, two = path[point][0], path[point+1][0]
                for i in range(min(one, two), max(one, two)+1):
                    scan[i][path[point][1]] = "#"

def pour_sand(x, y, floor):
    if scan[x][y] == "o":
        return False
    if y == max_y+1:
        if floor:
            scan[x][y] = "o"
            return True
        else:
            return False
    if scan[x][y+1] == ".":
        return pour_sand(x, y+1, floor)
    if scan[x-1][y+1] == ".":
        return pour_sand(x-1, y+1, floor)
    if scan[x+1][y+1] == ".":
        return pour_sand(x+1, y+1, floor)
    scan[x][y] = "o"
    return True


add_rock_formations()
while pour_sand(500, 0, False): pass
print("Silver:", count_stillsand())
while pour_sand(500, 0, True): pass
print("Gold:", count_stillsand())
