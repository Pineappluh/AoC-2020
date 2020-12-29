import fileinput
from collections import defaultdict


def parse_line(graph, line):
    data = line.strip().split(" contain ")
    parent_bag = data[0][:-1]  # bag instead of bags
    child_data = data[1][:-1]  # remove .

    for child_info in child_data.split(", "):
        if "no other bags" in child_info:
            continue

        count, child_bag = child_info.split(" ", 1)
        child_bag = child_bag.replace("bags", "bag")

        graph[parent_bag].append((child_bag, int(count)))


def dfs(current, size, graph, solution=0):
    for child, count in graph[current]:
        solution += count * size
        solution = dfs(child, count * size, graph, solution)

    return solution


graph = defaultdict(list)
for line in fileinput.input():
    parse_line(graph, line)

print(dfs("shiny gold bag", 1, graph))