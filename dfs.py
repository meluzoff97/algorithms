checked = []

def dfs(graph, x, y):
  global checked
  checked.append(x)
  if x == y:
    return True
  else:
    for i in graph[x]:
      if i not in checked:
        if dfs(graph, i, y):
         return True
  return False

#simple_graph = {'A' : ['B', 'C'],
#                'B' : ['D', 'C'],
#                'C' : ['A'],
#                'D' : ['E'],
#                'E' : []}