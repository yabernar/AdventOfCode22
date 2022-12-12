f = open("Day12/input", 'r')
elevation_map = []
start = None
end = None
for line in f:
    row = [* line.rstrip("\n")]
    if "S" in row:
        start = [len(elevation_map), row.index("S")]
    if "E" in row:
        end = [len(elevation_map), row.index("E")]
    elevation_map.append(row)
f.close()

# Part 1

elevations = "abcdefghijklmnopqrstuvwxyzE"
MAX_INT = 9999999

def print_map(distances_to_start):
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map[0])):
            if distances_to_start[i][j] <= 100:
                print(distances_to_start[i][j], end=" ")
            else:
                print(elevation_map[i][j], end="  ")
        print()

def get_possible_moves(node):
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    moves = []
    elevation = elevation_map[node[0]][node[1]]
    if elevation == "S": 
        elevation = "a"
    node_elevation = elevations.find(elevation)+1
    for d in directions:
        if 0 <= node[0]+d[0] < len(elevation_map) and 0 <= node[1]+d[1] < len(elevation_map[0]) and node_elevation >= elevations.find(elevation_map[node[0]+d[0]][node[1]+d[1]]):
            moves.append([node[0]+d[0], node[1]+d[1], node[2]+1])
    return moves

def key(node):
    return node[2]

def search(start):
    distances_to_start = [ [MAX_INT for _ in range(len(elevation_map[0]))] for _ in range(len(elevation_map))]
    to_evaluate = [[*start, 0]]
    distances_to_start[start[0]][start[1]] = 0
    while to_evaluate:
        current_node = to_evaluate.pop(0)
        moves = get_possible_moves(current_node)
        for m in moves:
            if distances_to_start[m[0]][m[1]] > m[2]:
                distances_to_start[m[0]][m[1]] = m[2]
                to_evaluate.append([m[0], m[1], m[2]])
        to_evaluate.sort(key=key)
    return distances_to_start[end[0]][end[1]]

print("Silver:", search(start))

# Part 2

best_scenic_start = MAX_INT
for i in range(len(elevation_map)):
    for j in range(len(elevation_map[0])):
        if elevation_map[i][j] == "a":
            best_scenic_start = min(best_scenic_start, search([i, j]))
print("Gold:", best_scenic_start)
