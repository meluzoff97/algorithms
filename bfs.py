def bfs(graph, x, y):
  queue = [x]
  checked = []
  while queue:
    v = queue.pop(0)
    if v == y:
      return True
    else:
      if not v in checked:
        queue.extend(graph[v])
        checked.append(v)
  return False

#simple_graph = {'A' : ['B', 'C'],
#                'B' : ['D', 'C'],
#                'C' : ['A'],
#                'D' : ['E'],
#                'E' : []}