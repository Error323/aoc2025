from re import findall
from collections import deque, defaultdict
from heapq import heappush, heappop
from functools import cache, reduce
from operator import add, mul, sub
import sys
import math

sys.setrecursionlimit(10000)

C4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C8 = C4 + [(1, 1), (-1, 1), (-1, -1), (1, -1)]
DIR4 = {c: d for c, d in zip(C4, "^>v<")}


def ints(s, negatives=True):
    if negatives:
        return list(map(int, findall(r"-?\d+", s)))
    else:
        return list(map(int, findall(r"\d+", s)))


def grid_from_string(s):
    g = [list(row.strip()) for row in s.split("\n") if row]
    return g, len(g), len(g[0])


def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0


def dijkstra(start, end, children):
    q = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    is_end = end if callable(end) else lambda x: x == end

    while q:
        cost, node = heappop(q)

        if is_end(node):
            path = []
            while node:
                path.append(node)
                node = came_from[node]
            return cost, path

        for child_cost, child in children(node):
            new_cost = cost + child_cost
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                heappush(q, (new_cost, child))
                came_from[child] = node

    return 0, []


def dijkstra_all(start, end, children):
    q = [(0, [start])]
    cost_so_far = {start: 0}
    is_end = end if callable(end) else lambda x: x == end
    paths = []

    while q:
        cost, path = heappop(q)
        node = path[-1]

        if is_end(node):
            paths.append((cost, path))

        for child_cost, child in children(node):
            new_cost = cost + child_cost
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                heappush(q, (new_cost, path + [child]))
            elif new_cost <= cost_so_far[child]:
                heappush(q, (new_cost, path + [child]))

    return sorted(paths)


def astar(start, end, children, heuristic):
    q = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    is_end = end if callable(end) else lambda x: x == end

    while q:
        _, node = heappop(q)
        cost = cost_so_far[node]

        if is_end(node):
            path = []
            while node:
                path.append(node)
                node = came_from[node]
            return cost, path

        for child_cost, child in children(node):
            new_cost = cost + child_cost
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                heappush(q, (new_cost + heuristic(child), child))
                came_from[child] = node

    return 0, []
