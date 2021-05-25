graph = [
    [1, 2],
    [3],
    [3],
    []
]
# graph = [
#   [1,3],
#   [0],
#   [3,8],
#   [0,2,4,5],
#   [3,6],
#   [3],
#   [4,7],
#   [6],
#   [2]
# ]

seen = [False for i in range(len(graph))]


def topologicalSort(graph, vertex, stack, seen):
    if seen[vertex]:
        return

    seen[vertex] = True

    for i in graph[vertex]:
        topologicalSort(graph, i, stack, seen)
    stack.append(vertex)


stack = []
for i in range(len(graph)):
    topologicalSort(graph, i, stack, seen)

while stack:
    print(stack.pop())
