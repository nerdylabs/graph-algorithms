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

seen = [False for i in range(len(adjacencyList))]


def traverseDFS(graph, vertex, seen, answer=[]):
    if seen[vertex]:
        return
    answer.append(vertex)
    seen[vertex] = True
    for i in graph[vertex]:
        traverseDFS(graph, i, seen, answer)
    return answer


print(traverseDFS(adjacencyList, 0, seen))
