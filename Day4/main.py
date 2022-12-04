f = open("Day4\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    pairs = word.split(",")
    pairs = pairs[0].split("-") + pairs[1].split("-")
    pairs = list(map(int, pairs))
    lst.append(pairs)
f.close()

# Part 1

fully_contained_pairs = 0
for pair in lst:
    if (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[2] >= pair[0] and pair[3] <= pair[1]):
        fully_contained_pairs += 1
print("Silver:", fully_contained_pairs)

# Part 2

overlapping_pairs = 0
for pair in lst:
    if pair[1] >= pair[2] and pair[3] >= pair[0]:
        overlapping_pairs += 1
print("Gold:", overlapping_pairs)