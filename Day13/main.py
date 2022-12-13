import functools

f = open("Day13/input", 'r')
packets = []
first = True
for line in f:
    row = line.rstrip("\n")
    if row == "": 
        first = True
        packets.append([left, right])
    elif first: 
        left = eval(row)
        first = False
    else:
        right = eval(row)
packets.append([left, right])
f.close()

# Part 1

def compare(left, right):
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]: return -1
            if left[i] > right[i]: return 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            sub = compare(left[i], right[i])
            if sub != 0: return sub
        elif isinstance(left[i], list):
            sub = compare(left[i], [right[i]])
            if sub != 0: return sub
        elif isinstance(right[i], list):
            sub = compare([left[i]], right[i])
            if sub != 0: return sub
    if len(left) == len(right): return 0
    if len(left) < len(right): return -1
    if len(left) > len(right): return 1

sum_correct_index = 0
for p in range(len(packets)):
    if compare(packets[p][0], packets[p][1]) == -1:
        sum_correct_index += p+1
print("Silver", sum_correct_index)

# Part 2

ordered_packets = [[[2]], [[6]]]
for p in packets:
    ordered_packets += p

ordered_packets.sort(key=functools.cmp_to_key(compare))
print("Gold:", (ordered_packets.index([[2]])+1) * (ordered_packets.index([[6]])+1))