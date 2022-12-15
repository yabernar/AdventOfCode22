def convert(value):
    return int(value[2:])

f = open("Day15/input", 'r')
sensors = []
beacons = []
for line in f:
    row = line.rstrip("\n").strip("Sensor at ").split(": closest beacon is at ")
    row[0] = row[0].split(", ")
    row[1] = row[1].split(", ")
    sensors.append([convert(row[0][0]), convert(row[0][1])])
    beacons.append([convert(row[1][0]), convert(row[1][1])])
f.close()


# Part 1
def md(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

target_line = 20
covered_positions = set()
for i in range(len(sensors)):
    d_beacon = md(sensors[i], beacons[i])
    d_line = md(sensors[i], [sensors[i][0], target_line])
    offset = 0
    while d_line+offset <= d_beacon:
        covered_positions.add(str(sensors[i][0]+offset)+","+str(target_line))
        covered_positions.add(str(sensors[i][0]-offset)+","+str(target_line))
        offset += 1

beacon_set = set()
for b in beacons:
    beacon_set.add(str(b[0])+","+str(b[1]))

print("Silver:", len(covered_positions) - len(covered_positions.intersection(beacon_set)))

# Part 2

def first(val):
    return val[0]

def search_line(target_line):
    covered_ranges = []
    for i in range(len(sensors)):
        d_beacon = md(sensors[i], beacons[i])
        d_line = md(sensors[i], [sensors[i][0], target_line])
        offset = d_beacon - d_line
        if offset >= 0:
            covered_ranges.append([sensors[i][0]-offset, sensors[i][0]+offset])
    covered_ranges.sort(key=first)
    c_max = 0
    for r in covered_ranges:
        if r[0] <= c_max:
            c_max = max(c_max, r[1])
        else:
            print("Gold:", (c_max+1)*4000000 + target_line)
            return False
    return True

line = 0
while line <= 4000000 and search_line(line):line += 1