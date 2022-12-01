f = open("Day1\input", 'r')
lst = []
total_cal = 0
for line in f:
    word = line.rstrip("\n")
    if word == "":
        lst.append(total_cal)
        total_cal = 0
    else:
        total_cal += int(word)
f.close()

# Part 1

print("Highest calories on an elf: ", max(lst))

# Part 2

lst.sort()
lst.reverse()
print("Top three calories: ", sum(lst[0:3]))