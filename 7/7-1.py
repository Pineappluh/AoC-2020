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

        graph[child_bag].append(parent_bag)


def dfs(current, graph, visited=set()):
    visited.add(current)

    for parent in graph[current]:
        if parent not in visited:
            dfs(parent, graph, visited)

    return visited


graph = defaultdict(list)
for line in fileinput.input():
    parse_line(graph, line)

parents = dfs("shiny gold bag", graph)
print(len(parents) - 1)
