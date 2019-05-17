# pylint: disable=invalid-name, multiple-statements, fixme, missing-docstring, bad-indentation
def main():
  from sys import stdout
  n, t = map(int, input().split(' '))
  sched = dict()
  for _ in range(n):
    s, d = map(int, input().split(' '))
    sched[s] = d

  def solve(sched, t):
    rets = dict()
    for k, v in sched.items():
      if k == t:
        return list(sched.keys()).index(k) + 1

    for k, v in sched.items():
      interval = float("inf")
      if t < k:
        _k = k
        while t <= k:
          tmp = abs(t - k)
          if tmp < interval:
            interval = tmp
          t += v
        rets[_k] = interval
      elif t > k:
        interval = float("inf")
        _k = k
        while t >= k:
          tmp = abs(t - k)
          if tmp < interval:
            interval = tmp
          k += v
        rets[_k] = interval

    min_interval = min(rets, key=rets.get)
    # print(rets)
    return list(sched.keys()).index(min_interval) + 1
  w = stdout.write
  w('%d\n' % solve(sched, t))

main()
