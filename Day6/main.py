f = open("Day6\input", 'r')
message = ""
for line in f:
    message = line.rstrip("\n")
f.close()

# Part 1

for i in range(len(message)):
    if (message[i] not in message[i+1:i+4]) and (message[i+1] not in message[i+2:i+4]) and message[i+2] != message[i+3]:
        print("Silver :", i+4)
        break

# Part 2

offset = 14
for i in range(len(message)):
    repeat = False
    for j in range(i, i+offset-1):
        if message[j] in message[j+1:i+offset]:
            repeat = True
            break
    if not repeat:
        print("Gold :", i+offset)
        break
