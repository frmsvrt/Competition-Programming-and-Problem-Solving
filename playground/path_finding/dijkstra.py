#!/usr/bin/env python3
# Dijkastra alg based on heap queue
# With adjacency-list representation,
# and adjacency matrix one
# mostly based on https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm
from collections import defaultdict
from heapq import heappop, heappush

class Graph():
  # class for adjacency path representation
  # and min distance solving

  def __init__(self, verticies):
    self.V = verticies
    self.graph = [[0 for col in range(verticies)] for row in range(verticies)]

  def minDistance(self, dist, setV):
    min_dist = float("inf")
    for verticie in range(self.V):
      if dist[verticie] < min_dist and setV[verticie] == False:
        min_dist = dist[verticie]
        min_index = verticie

    return min_index

  def solve(self, start):
    dist = [float("inf")] * self.V
    dist[start] = 0
    setV = [False] * self.V
    for cout in range(self.V):
      u = self.minDistance(dist, setV)
      setV[u] = True
      for v in range(self.V):
        if self.graph[u][v] > 0 and setV[v] == False and dist[v] > dist[u] + self.graph[u][v]:
          dist[v] = dist[u] + self.graph[u][v]

    for node in range(self.V):
      print(node, "t", dist[node])

    return

def dijkstra(edges, f, t):
  g = defaultdict(list)
  for l, r, c in edges:
    g[l].append((c, r))

  q, seen, dist = [(0, f, ())], set(), {f: 0}
  while q:
    (cost, v1, path) = heappop(q)
    if v1 not in seen:
      seen.add(v1)
      path += (v1,)
      if v1 == t: return (cost, path)

      for c, v2 in g.get(v1, ()):
        if v2 in seen: continue

        if v2 not in dist or cost + c < dist[v2]:
          dist[v2] = cost + c
          heappush(q, (cost+c, v2, path))

  return float("inf")


if __name__ == "__main__":
  edges = [
      ("A", "B", 7),
      ("A", "D", 5),
      ("B", "C", 8),
      ("B", "D", 9),
      ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15),
      ("D", "F", 6),
      ("E", "F", 8),
      ("E", "G", 9),
      ("F", "G", 11)
      ]

  print("A -> E:")
  print(dijkstra(edges, "A", "E"))
  print("A -> G:")
  print(dijkstra(edges, "A", "G"))
  
  g  = Graph(9)
  g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]];

  g.solve(0)
