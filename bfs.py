def bfs(graph, x, y):
  queue = graph[x][:]
  checked = []
  while queue:
    v = queue.pop(0)
    if v == y:
      return True
    else:
      queue.extend(graph[v])
      checked.append(v)
  return False

#simple_graph = {'A' : ['B', 'C'],
#                'B' : ['D', 'C'],
#                'C' : ['A'],
#                'D' : ['E'],
#                'E' : []}