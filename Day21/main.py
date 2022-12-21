f = open("Day21/input", 'r')
monkeys = {}
for line in f:
    says = line.strip("\n").split(": ")
    monkeys[says[0]] = says[1]
f.close()

# Part 1
def find_out(monkey_name):
    if "+" in monkeys[monkey_name]:
        parts = monkeys[monkey_name].split(" + ")
        return find_out(parts[0]) + find_out(parts[1])
    if "-" in monkeys[monkey_name]:
        parts = monkeys[monkey_name].split(" - ")
        return find_out(parts[0]) - find_out(parts[1])
    if "*" in monkeys[monkey_name]:
        parts = monkeys[monkey_name].split(" * ")
        return find_out(parts[0]) * find_out(parts[1])
    if "/" in monkeys[monkey_name]:
        parts = monkeys[monkey_name].split(" / ")
        return find_out(parts[0]) // find_out(parts[1])
    return int(monkeys[monkey_name])

print("Silver:", find_out("root"))

# Part 2
def add(one, two):return one+two
def sub(one, two):return one-two
def sub2(one, two):return two-one
def mul(one, two):return one*two
def div(one, two):return one//two

operators = {" + ": add, " - ": sub, " * ": mul, " / ": div}
reverse = {" + ": sub, " - ": add, " * ": div, " / ": mul}

def find_out_two(monkey_name, value):
    if monkey_name == "humn": 
        if value is not None: 
            print("Gold:", value)
        else:
            return None
    for op in operators:
        if op in monkeys[monkey_name]:
            parts = monkeys[monkey_name].split(op)
            one = find_out_two(parts[0], None)
            two = find_out_two(parts[1], None)
            if value is None and (one is None or two is None):
                return None
            if one is None:
                return find_out_two(parts[0], reverse[op](value, two))
            if two is None:
                if op == " / ":
                    return find_out_two(parts[1], div(one, value))
                if op == " - ":
                    return find_out_two(parts[1], sub(one, value))
                return find_out_two(parts[1], reverse[op](value, one))
            return operators[op](one, two)
    return int(monkeys[monkey_name])

parts = monkeys["root"].split(" + ")
one = find_out_two(parts[0], None)
two = find_out_two(parts[1], None)
if one is None:
    find_out_two(parts[0], two)
else:
    find_out_two(parts[1], one)
