import numpy as np

def solve(sched, t):
  intervals = []
  closests = []
  rets = dict()
  for k, v in sched.items():
    if k == t:
      return list(sched.keys()).index(k) + 1

  for k, v in sched.items():
    interval = float("inf")
    if t < k:
      _k = k
      while t < k:
        t += v
        tmp = np.abs(t - k)
        if tmp < interval:
          interval = tmp
      rets[_k] = interval
    elif t > k:
      interval = float("inf")
      _k = k
      while t > k:
        tmp = np.abs(t - k)
        if tmp < interval:
          interval = tmp
        k += v
      rets[_k] = interval

  min_interval = min(rets, key=rets.get)
  return list(sched.keys()).index(min_interval) + 1
  

n, t = map(int, input().split())
sched = dict()
for i in range(n):
  s, d = map(int, input().split())
  sched[s] = d

print(solve(sched, t))
