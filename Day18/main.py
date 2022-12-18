f = open("Day18/input", 'r')
blocks = []
for line in f:
    pos = [*map(int, line.rstrip("\n").split(","))]
    blocks.append(pos)
f.close()

# Part 1:
faces = 0
for b in blocks:
    if [b[0]+1, b[1], b[2]] not in blocks: faces += 1
    if [b[0]-1, b[1], b[2]] not in blocks: faces += 1
    if [b[0], b[1]+1, b[2]] not in blocks: faces += 1
    if [b[0], b[1]-1, b[2]] not in blocks: faces += 1
    if [b[0], b[1], b[2]+1] not in blocks: faces += 1
    if [b[0], b[1], b[2]-1] not in blocks: faces += 1

print("Silver:", faces)

# Part 2:
water_square = []
unexplored_squares = [[0,0,0]]

def spread_water(p):
    if p not in water_square and p not in blocks and p not in unexplored_squares:
        unexplored_squares.append(p)

while unexplored_squares:
    p = unexplored_squares.pop()
    if p not in water_square and p not in blocks:
        water_square.append(p)
        if p[0]+1 <= 23: spread_water([p[0]+1, p[1], p[2]])
        if p[0]-1 >= -3 : spread_water([p[0]-1, p[1], p[2]])
        if p[1]+1 <= 23: spread_water([p[0], p[1]+1, p[2]])
        if p[1]-1 >= -3 : spread_water([p[0], p[1]-1, p[2]])
        if p[2]+1 <= 23: spread_water([p[0], p[1], p[2]+1])
        if p[2]-1 >= -3 : spread_water([p[0], p[1], p[2]-1])

faces = 0
for b in blocks:
    if [b[0]+1, b[1], b[2]] in water_square: faces += 1
    if [b[0]-1, b[1], b[2]] in water_square: faces += 1
    if [b[0], b[1]+1, b[2]] in water_square: faces += 1
    if [b[0], b[1]-1, b[2]] in water_square: faces += 1
    if [b[0], b[1], b[2]+1] in water_square: faces += 1
    if [b[0], b[1], b[2]-1] in water_square: faces += 1

print("Gold:", faces)