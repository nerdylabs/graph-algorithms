# graph = [
#   [1],
#   [2],
#   [0],
#   [0]
# ]

# graph = [
#   [1,2],
#   [2],
#   [],
#   [0]
# ]

graph = [
  [1], 
  [0]
]


def hasCycle(graph, vertex, visited, visiting):
  visiting.append(vertex)
  for i in graph[vertex]:
    if i in visited:
      continue
    
    if i in visiting:
      return True
    if hasCycle(graph, i, visited, visiting):
      return True
  visiting.remove(vertex)
  visited.append(vertex)
  return False


for i in range(len(graph)):
  print(hasCycle(graph, i, [], []))


# print(hasCycle(graph, 0, [], []))