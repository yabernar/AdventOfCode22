import math
import copy

f = open("Day19/input", 'r')
blueprints = []
for line in f:
    line = line.strip("\n").split()
    bp = {"ore":int(line[6]), "clay":int(line[12]), "obsidian":[int(line[18]), int(line[21])], "geode":[int(line[27]), int(line[30])]}
    blueprints.append(bp)
f.close()

# Part 1
def ceil_division(n, d):
    return -(n // -d)

def upper_bound(geodes, robots, time_left):
    if time_left > 0:
        return geodes + robots*time_left + math.factorial(time_left-1)
    return geodes

def add_robot(bp, robots, resources, robot_type):
    robots[robot_type] += 1
    if robot_type == "ore":
        resources["ore"] -= bp["ore"]
    elif robot_type == "clay":
        resources["ore"] -= bp["clay"]
    elif robot_type == "obsidian":
        resources["ore"] -= bp["obsidian"][0]
        resources["clay"] -= bp["obsidian"][1]
    elif robot_type == "geode":
        resources["ore"] -= bp["geode"][0]
        resources["obsidian"] -= bp["geode"][1]
    return robots, resources

def add_resources(robots, resources, time):
    resources["ore"] += robots["ore"]*time
    resources["clay"] += robots["clay"]*time
    resources["obsidian"] += robots["obsidian"]*time
    resources["geode"] += robots["geode"]*time
    return resources

def process_blueprint(bp, robots, resources, time_left, robot_caps, best):
    open_geodes = 0
    if upper_bound(resources["geode"], robots["geode"], time_left) <= best: return resources["geode"]
    # Next robot is geode:
    if robots["obsidian"] > 0:
        time_necessary = 1 + max(ceil_division(bp["geode"][0] - resources["ore"], robots["ore"]), ceil_division(bp["geode"][1] - resources["obsidian"], robots["obsidian"]))
        if time_necessary < 1: time_necessary = 1
        if time_necessary <= time_left:
            new_resources = add_resources(robots, copy.deepcopy(resources), time_necessary)
            new_robots, new_resources = add_robot(bp, copy.deepcopy(robots), new_resources, "geode")
            open_geodes = max(open_geodes, process_blueprint(bp, new_robots, new_resources, time_left-time_necessary, robot_caps, best))
            best = max(open_geodes, best)
    # Next robot is obsidian:
    if robots["clay"] > 0:
        time_necessary = 1 + max(ceil_division(bp["obsidian"][0] - resources["ore"], robots["ore"]), ceil_division(bp["obsidian"][1] - resources["clay"], robots["clay"]))
        if time_necessary < 1: time_necessary = 1
        if time_necessary <= time_left and robots["obsidian"] < robot_caps["obsidian"]:
            new_resources = add_resources(robots, copy.deepcopy(resources), time_necessary)
            new_robots, new_resources = add_robot(bp, copy.deepcopy(robots), new_resources, "obsidian")
            open_geodes = max(open_geodes, process_blueprint(bp, new_robots, new_resources, time_left-time_necessary, robot_caps, best))
            best = max(open_geodes, best)
    # Next robot is clay:
    time_necessary = 1 + ceil_division(bp["clay"] - resources["ore"], robots["ore"])
    if time_necessary < 1: time_necessary = 1
    if time_necessary <= time_left and robots["clay"] < robot_caps["clay"]:
        new_resources = add_resources(robots, copy.deepcopy(resources), time_necessary)
        new_robots, new_resources = add_robot(bp, copy.deepcopy(robots), new_resources, "clay")
        open_geodes = max(open_geodes, process_blueprint(bp, new_robots, new_resources, time_left-time_necessary, robot_caps, best))
        best = max(open_geodes, best)
    # Next robot is ore:
    time_necessary = 1 + ceil_division(bp["ore"] - resources["ore"], robots["ore"])
    if time_necessary < 1: time_necessary = 1
    if time_necessary <= time_left and robots["ore"] < robot_caps["ore"]:
        new_resources = add_resources(robots, copy.deepcopy(resources), time_necessary)
        new_robots, new_resources = add_robot(bp, copy.deepcopy(robots), new_resources, "ore")
        open_geodes = max(open_geodes, process_blueprint(bp, new_robots, new_resources, time_left-time_necessary, robot_caps, best))
        best = max(open_geodes, best)
    resources = add_resources(robots, resources, time_left)
    return max(open_geodes, resources["geode"])    
    
bp_nbr = 1
quality = 0
for bp in blueprints:
    print("Blueprint:", bp_nbr,"/",len(blueprints))
    cap = {"ore":max(bp["ore"], bp["clay"], bp["obsidian"][0], bp["geode"][0]), "clay":bp["obsidian"][1], "obsidian":bp["geode"][1]}
    gd = process_blueprint(bp, {"ore":1, "clay":0, "obsidian":0, "geode":0}, {"ore":0, "clay":0, "obsidian":0, "geode":0}, 24, cap, 0)
    quality += bp_nbr * gd
    bp_nbr += 1
print("Silver:", quality)

# Part 2

quality = 1
bp_nbr = 1
for bp in blueprints[0:3]:
    print("Blueprint:", bp_nbr,"/3")
    cap = {"ore":max(bp["ore"], bp["clay"], bp["obsidian"][0], bp["geode"][0]), "clay":bp["obsidian"][1], "obsidian":bp["geode"][1]}
    gd = process_blueprint(bp, {"ore":1, "clay":0, "obsidian":0, "geode":0}, {"ore":0, "clay":0, "obsidian":0, "geode":0}, 32, cap, 0)
    quality *= gd
    bp_nbr += 1
print("Gold:", quality)
