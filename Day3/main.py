f = open("Day3\input", 'r')
lst = []
lst2 = []
for line in f:
    word = line.rstrip("\n")
    halves = [word[0:len(word)//2], word[len(word)//2:len(word)]]
    lst.append(halves)
    lst2.append(word)
f.close()

# Part 1

items = ""
for rucksack in lst:
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            items += letter
            break

priorities_order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priorities_sum = 0
for letter in items:
    priorities_sum += priorities_order.find(letter)+1
print("Items priorities sum:", priorities_sum)

# Part 2

badges = ""
for i in range(0, len(lst2), 3):
    for letter in lst2[i]:
        if letter in lst2[i+1] and letter in lst2[i+2]:
            badges += letter
            break

priorities_sum = 0
for letter in badges:
    priorities_sum += priorities_order.find(letter)+1
print("Badges priorities sum:", priorities_sum)