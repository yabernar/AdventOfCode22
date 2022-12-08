f = open("Day8\input", 'r')
forest = []
for line in f:
    letters = [*line.rstrip("\n")]
    letters = list(map(int, letters))
    forest.append(letters)
f.close()

# Part 1

visible_trees = []

def add_visible_trees(start, stop, step, i, horizontal):
    tree_size = -1
    for j in range(start, stop, step):
        if horizontal:
            x, y = i, j
        else:
            x, y = j, i
        if forest[x][y] > tree_size:
            tree_size = forest[x][y]
            tree = str(x)+"-"+str(y)
            if tree not in visible_trees:
                visible_trees.append(tree)

for i in range(0, len(forest)):
    add_visible_trees(0, len(forest[i]), 1, i, True)
    add_visible_trees(len(forest[i])-1, 0, -1, i, True)
for j in range(0, len(forest[0])):
    add_visible_trees(0, len(forest), 1, j, False)
    add_visible_trees(len(forest)-1, 0, -1, j, False)

print("Silver:", len(visible_trees))

# Part 2

def search(x, y, dx, dy, height):
    if x > 0 and x < len(forest[0])-1 and y > 0 and y < len(forest)-1 and forest[x][y] < height:
        return 1 + search(x+dx, y+dy, dx, dy, height)
    return 1

def scenic_score(x, y):
    tree_size = forest[x][y]
    return search(x+1, y, 1, 0, tree_size) * search(x-1, y, -1, 0, tree_size) * search(x, y+1, 0, 1, tree_size) * search(x, y-1, 0, -1, tree_size)

scores = []
for i in range(len(forest[0])):
    for j in range(len(forest)):
        scores.append(scenic_score(i,j))
print("Gold:", max(scores))