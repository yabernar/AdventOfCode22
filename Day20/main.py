import copy

f = open("Day20/input", 'r')
lst = []
for line in f:
    nbr = line.strip("\n")
    while nbr in lst:
        nbr += "a"
    lst.append(nbr)
f.close()

# Part 1
def to_int(s):
    return int(s.rstrip("a"))

def mixing(lst, order):
    for item in order:
        position = lst.index(item)
        lst.pop(position)
        position = (position+to_int(item))%(len(lst))
        lst.insert(position, item)

order = copy.deepcopy(lst)
mixing(lst, order)
zero_pos = lst.index("0")
print("Silver:", to_int(lst[(1000+zero_pos)%len(lst)])+to_int(lst[(2000+zero_pos)%len(lst)])+to_int(lst[(3000+zero_pos)%len(lst)]))

# Part 2
lst = copy.deepcopy(order)
key = 811589153
for i in range(len(lst)):
    lst[i] = str(to_int(lst[i])*key)+"a"*lst[i].count("a")

order = copy.deepcopy(lst)
for _ in range(10):
    mixing(lst, order)
zero_pos = lst.index("0")
print("Gold:", to_int(lst[(1000+zero_pos)%len(lst)])+to_int(lst[(2000+zero_pos)%len(lst)])+to_int(lst[(3000+zero_pos)%len(lst)]))
