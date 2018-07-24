#!/usr/bin/env python3
# Dijkastra alg based on heap queue
# With adjacency-list representation
from collections import defaultdict
from heapq import heappop, heappush

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
