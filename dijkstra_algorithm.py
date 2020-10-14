def dijkstra_algorithm(graph, x, y):
  infinity = float("inf")
  costs = {}
  parents = {}
  checked = []

  costs[y] = infinity
  parents[y] = None
  neighbors = graph[x]
  for n in neighbors.keys():
    costs[n] = neighbors[n]  
    parents[n] = x
  
  min_cost = costs[y]
  node = y
  for n in costs.keys():
    if costs[n] < min_cost:
      min_cost = costs[n]
      node = n
  
  if min_cost == infinity:
    return None
  elif node == y:
    return {'path': [x,y], 'cost': costs[y]}
  else:
    while node:
      cost = costs[node]
      neighbors = graph[node]
      for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if not costs.get(n):
          costs[n] = new_cost
          parents[n] = node
        elif new_cost < costs[n]:
          costs[n] = new_cost
          parents[n] = node
      checked.append(node)
      min_cost = infinity
      node = None
      for n in costs.keys():
        if costs[n] < min_cost and n not in checked:
          min_cost = costs[n]
          node = n
    if costs[y] == infinity:
      return None
    node = y
    path = [node]
    while node != x:
      node = parents[node]
      path.append(node) 
    return {'path': list(reversed(path)), 'cost': costs[y]}

#simple_graph = {'A' : {'B': 30, 'E' : 100},
#                'B' : {'C' : 30},
#                'C' : {'D' : 30},
#                'D' : {'F' : 30},
#                'E' : {'F' : 10},
#                'F' : {'G' : 10},
#                'G' : {}}