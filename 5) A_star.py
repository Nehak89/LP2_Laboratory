# # A* Search - Simple Version with User Input

# n = int(input("Enter number of edges: "))
# graph = {}

# print("Enter edges in format: node1 node2 cost")
# for _ in range(n):
#     u, v, cost = input().split()
#     cost = int(cost)
#     if u not in graph:
#         graph[u] = {}
#     graph[u][v] = cost

# heuristic = {}
# nodes = set(graph.keys())
# for edges in graph.values():
#     nodes.update(edges.keys())

# print("Enter heuristic for each node:")
# for node in nodes:
#     heuristic[node] = int(input(f"Heuristic for {node}: "))

# start = input("Enter start node: ")
# goal = input("Enter goal node: ")

# open_list = [start]
# g = {start: 0}
# parent = {start: None}

# while open_list:
#     current = min(open_list, key=lambda x: g[x] + heuristic[x])
#     open_list.remove(current)

#     if current == goal:
#         break

#     for neighbor in graph.get(current, {}):
#         temp_g = g[current] + graph[current][neighbor]
#         if neighbor not in g or temp_g < g[neighbor]:
#             g[neighbor] = temp_g
#             parent[neighbor] = current
#             open_list.append(neighbor)

# path = []
# node = goal
# while node:
#     path.append(node)
#     node = parent.get(node)
# path.reverse()
# print("Path:", path)

n = int(input("Enter number of edges: "))
graph = {}
print("Enter edges in format: node1 node2 cost")
for _ in range(n):
    u, v, c = input().split(); graph.setdefault(u, {})[v] = int(c)

nodes = set(graph.keys()) | {v for edges in graph.values() for v in edges}
print("Enter heuristic for each node:")
heuristic = {node: int(input(f"Heuristic for ({node}): ")) for node in nodes}
start, goal = input("Start: "), input("Goal: ")

g, parent, open_list = {start: 0}, {start: None}, [start]
while open_list:
    current = min(open_list, key=lambda x: g[x] + heuristic[x])
    open_list.remove(current)
    if current == goal: break
    for neighbor, cost in graph.get(current, {}).items():
        if neighbor not in g or (g[current] + cost) < g[neighbor]:
            g[neighbor] = g[current] + cost
            parent[neighbor] = current
            open_list.append(neighbor)

path = []
while goal: path.append(goal); goal = parent[goal]
print("Path:", path[::-1])
