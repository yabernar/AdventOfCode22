import copy

monkey_list = []
monkey_list.append({"items": [71, 56, 50, 73], "operation": "*", "value": 11, "divisible_by": 13, True: 1, False: 7})
monkey_list.append({"items": [70, 89, 82], "operation": "+", "value": 1, "divisible_by": 7, True: 3, False: 6})
monkey_list.append({"items": [52, 95], "operation": "**", "divisible_by": 3, True: 5, False: 4})
monkey_list.append({"items": [94, 64, 69, 87, 70], "operation": "+", "value": 2, "divisible_by": 19, True: 2, False: 6})
monkey_list.append({"items": [98, 72, 98, 53, 97, 51], "operation": "+", "value": 6, "divisible_by": 5, True: 0, False: 5})
monkey_list.append({"items": [79], "operation": "+", "value": 7, "divisible_by": 2, True: 7, False: 0})
monkey_list.append({"items": [77, 55, 63, 93, 66, 90, 88, 71], "operation": "*", "value": 7, "divisible_by": 11, True: 2, False: 4})
monkey_list.append({"items": [54, 97, 87, 70, 59, 82, 59], "operation": "+", "value": 8, "divisible_by": 17, True: 1, False: 3})

monkey_list_2 = copy.deepcopy(monkey_list)

# Part 1
monkey_business = [0] * 8

for i in range(20):
    current_monkey = 0
    for m in monkey_list:
        for item in m["items"]:
            if m["operation"] == "*":
                new_worry = item * m["value"]
            elif m["operation"] == "+":
                new_worry = item + m["value"]
            else:
                new_worry = item ** 2
            new_worry = new_worry // 3
            monkey_list[m[new_worry % m["divisible_by"] == 0]]["items"].append(new_worry)
        monkey_business[current_monkey] += len(m["items"])
        current_monkey += 1
        m["items"] = []

monkey_business.sort()
monkey_business.reverse()
print("Silver:", monkey_business[0] * monkey_business[1])

# Part 2
monkey_business = [0] * 8
offset = 1
for m in monkey_list_2:
    offset *= m["divisible_by"]

for i in range(10000):
    current_monkey = 0
    for m in monkey_list_2:
        for item in m["items"]:
            if m["operation"] == "*":
                new_worry = item * m["value"]
            elif m["operation"] == "+":
                new_worry = item + m["value"]
            else:
                new_worry = item ** 2
            new_worry = new_worry % offset
            monkey_list_2[m[new_worry % m["divisible_by"] == 0]]["items"].append(new_worry)
        monkey_business[current_monkey] += len(m["items"])
        current_monkey += 1
        m["items"] = []

monkey_business.sort()
monkey_business.reverse()
print("Gold:", monkey_business[0] * monkey_business[1])