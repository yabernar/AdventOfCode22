import copy

f = open("Day16/input", 'r')
valves = {}
for line in f:
    valve = line.rstrip("\n")[6:].split(" has flow rate=")
    flow_rate = valve[1].split(";")
    tunnels = flow_rate[1].strip(" tunnels lead to valves").split(", ")
    valves[valve[0]] = {"flow rate":int(flow_rate[0]), "tunnels":tunnels}
f.close()

# Part 1
INFINITY = 99999999
distances = {}
for v in valves.keys():
    distances[v] = {}
    for w in valves.keys():
        dist = INFINITY
        if v == w:
            dist = 0
        if v in valves[w]["tunnels"]:
            dist = 1
        distances[v][w] = dist

def floyd_warshall():
    for k in valves.keys():   
        for i in valves.keys():
            for j in valves.keys():
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

floyd_warshall()
# for i in valves.keys():
#     print(i, valves[i], "\t\t", distances[i])

def sorting_by_flow_rate(valve):
    return valves[valve]["flow rate"]

closed_valves = []
for v in valves.keys():
    if valves[v]["flow rate"] > 0:
        closed_valves.append(v)
closed_valves.sort(key=sorting_by_flow_rate)
closed_valves.reverse()

def best_pressure_release(current_valve, closed_valves, remaining_time):
    if closed_valves == [] or remaining_time == 0:
        return 0
    max_pressure = 0
    for v in closed_valves:
        time_left = remaining_time - 1 - distances[current_valve][v]
        if  time_left > 0:
            new_closed_valves = copy.deepcopy(closed_valves)
            new_closed_valves.remove(v)
            released_pressure = valves[v]["flow rate"]*time_left + best_pressure_release(v, new_closed_valves, time_left)
            max_pressure = max(max_pressure, released_pressure)
    return max_pressure

max_pressure = best_pressure_release("AA", closed_valves, 30)
print("Silver:", max_pressure)

# Part 2

def best_pressure_with_elephant(my_valve, my_time, elephant_valve, elephant_time, closed_valves, remaining_time):
    # if remaining_time == 26:
    #     print(my_valve, elephant_valve, remaining_time)
    if closed_valves == [] or remaining_time == 0:
        return 0
    if my_time > 0 and elephant_time > 0:
        return best_pressure_with_elephant(my_valve, my_time-1, elephant_valve, elephant_time-1, closed_valves, remaining_time-1)
    # max_pressure = 0
    # if my_time == 0:
    #     for v in closed_valves:
    #         time_left = remaining_time - 1 - distances[my_valve][v]
    #         if  time_left > 0:
    #             new_closed_valves = copy.deepcopy(closed_valves)
    #             new_closed_valves.remove(v)
    #             released_pressure = valves[v]["flow rate"]*time_left + best_pressure_with_elephant(v, 1 + distances[my_valve][v], elephant_valve, elephant_time, new_closed_valves, remaining_time)
    #             max_pressure = max(max_pressure, released_pressure)
    # if elephant_time == 0 and not (my_time == 0 and my_valve == elephant_valve):
    #     for v in closed_valves:
    #         time_left = remaining_time - 1 - distances[elephant_valve][v]
    #         if  time_left > 0:
    #             new_closed_valves = copy.deepcopy(closed_valves)
    #             new_closed_valves.remove(v)
    #             released_pressure = valves[v]["flow rate"]*time_left + best_pressure_with_elephant(my_valve, my_time, v, 1 + distances[elephant_valve][v], new_closed_valves, remaining_time)
    #             max_pressure = max(max_pressure, released_pressure)
    # return max_pressure

    if my_time == 0 or elephant_time == 0:
        max_pressure = 0
        for v in closed_valves:
            if (my_time == 0 and elephant_time == 0 and distances[my_valve][v] > distances[elephant_valve][v]) or my_time != 0:
                priority_elephant = True
            else:
                priority_elephant = False
            if priority_elephant: time_left = remaining_time - 1 - distances[elephant_valve][v]
            else: time_left = remaining_time - 1 - distances[my_valve][v]
            if  time_left > 0:
                new_closed_valves = copy.deepcopy(closed_valves)
                new_closed_valves.remove(v)
                if priority_elephant: released_pressure = valves[v]["flow rate"]*time_left + best_pressure_with_elephant(my_valve, my_time, v, 1 + distances[elephant_valve][v], new_closed_valves, remaining_time)
                else: released_pressure = valves[v]["flow rate"]*time_left + best_pressure_with_elephant(v, 1 + distances[my_valve][v], elephant_valve, elephant_time, new_closed_valves, remaining_time)
                max_pressure = max(max_pressure, released_pressure)
        return max_pressure

max_pressure = best_pressure_with_elephant("AA", 0, "AA", 0, closed_valves, 26)
print("Gold:", max_pressure)
