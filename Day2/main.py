f = open("Day2\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(word)
f.close()

# Part 1

score_sheet = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

total_score = 0
for game_round in lst:
    total_score += score_sheet[game_round]
print("Total score, part 1:", total_score)

# Part 2

score_sheet = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

total_score = 0
for game_round in lst:
    total_score += score_sheet[game_round]
print("Total score, part 2:", total_score)