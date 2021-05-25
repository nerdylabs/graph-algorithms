adjacencyList = [
    [1, 3],
    [0],
    [3, 8],
    [0, 2, 4, 5],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]


def taraverseBFS(graph):
    seen = [False for i in range(len(graph))]
    bfs = []
    queue = [0]
    i = 1
    while len(queue):
        curr_node = queue.pop(0)
        bfs.append(curr_node)
        seen[curr_node] = True

        connections = graph[curr_node]
        for i in connections:
            if not seen[i]:
                queue.append(i)
    return bfs


print(taraverseBFS(adjacencyList))
