f = open("Day10/input", 'r')
program = []
for line in f:
    instruction = line.rstrip("\n").split(" ")
    if instruction[0] == "addx":
        instruction[1] = int(instruction[1])
    program.append(instruction)
f.close()

# Part 1

x_register = 1
cycle_count = 0
signal_strenght = 0
for instruction in program:
    cycle_count += 1
    if (cycle_count-20)%40 == 0:
        signal_strenght += x_register*cycle_count
    if instruction[0] == "addx":
        x_register += instruction[1]
        cycle_count += 1

print("Silver:", signal_strenght)

# Part 2

crt_display = [ ["_" for _ in range(40) ] for _ in range(6) ]

x_register = 1
instruction_head = 0
first_cycle = True
for position in range(240):
    if x_register - 1 <= position%40 <= x_register + 1:
        crt_display[position//40][position%40] = "#"
    else: 
        crt_display[position//40][position%40] = "."
    if instruction_head >= len(program):
        pass
    elif program[instruction_head][0] == "noop":
        instruction_head += 1
    elif program[instruction_head][0] == "addx":
        if first_cycle: first_cycle = False
        else: 
            x_register += program[instruction_head][1]
            instruction_head += 1
            first_cycle = True

def print_display():
    for i in crt_display:
        for j in i:
            print(j, end="")
        print()

print("Gold:")
print_display()