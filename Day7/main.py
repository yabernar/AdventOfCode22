f = open("Day7\input", 'r')
commands = []
idx = -1
for line in f:
    word = line.rstrip("\n").split(" ")
    if word[0] == "$":
        commands.append([word])
        idx +=1
    else:
        commands[idx].append(word)
f.close()

# Populating tree

root = {
    "type": "dir",
    "name": "/",
    "size": 0,
    "parent": None,
    "children": {}
}

current_location = root

for cmd in commands:
    if cmd[0][1] == "cd":
        if cmd[0][2] == "..":
            current_location = current_location["parent"]
        else:
            current_location = current_location["children"][cmd[0][2]]
    elif cmd[0][1] == "ls":
        for element in cmd[1:]:
            if element[0] == "dir":
                new_dir = {
                    "type": "dir",
                    "name": element[1],
                    "size": 0,
                    "parent": current_location,
                    "children": {}
                }
                current_location["children"][element[1]] = new_dir
            else:
                new_file = {
                    "type": "file",
                    "name": element[1],
                    "size": int(element[0]),
                    "parent": current_location
                }
                current_location["children"][element[1]] = new_file

def recursive_print(location, depth):
    if location["type"] == "dir":
        print("  "*depth, "-", location["name"], "(dir, size="+str(location["size"])+")")
        for child in location["children"].values():
            recursive_print(child, depth+1)
    else:
        print("  "*depth, "-", location["name"], "(file, size="+str(location["size"])+")")

def recursive_dir_size_filling(location):
    if location["type"] == "dir":
        location["size"] = 0
        for child in location["children"].values():
            location["size"] += recursive_dir_size_filling(child)
        return location["size"]
    else:
        return location["size"]

recursive_dir_size_filling(root)

# Part 1

def recursive_find_low_size_folders(location):
    if location["type"] == "dir":
        if location["size"] <= 100000:
            total_sum = location["size"]
        else:
            total_sum = 0
        for child in location["children"].values():
            total_sum += recursive_find_low_size_folders(child)
        return total_sum
    return 0

print("Silver:", recursive_find_low_size_folders(root))

# Part 2

MAX_INT = 70000000

def recursive_find_closest_size_folder(location, necessary_space):
    if location["type"] == "dir":
        solutions = []
        if location["size"] >= necessary_space:
            solutions.append(location["size"])
        for child in location["children"].values():
            solutions.append(recursive_find_closest_size_folder(child, necessary_space))
        return min(solutions)
    return MAX_INT

space_to_be_liberated = 30000000 - (70000000 - root["size"])
print("Gold:", recursive_find_closest_size_folder(root, space_to_be_liberated))