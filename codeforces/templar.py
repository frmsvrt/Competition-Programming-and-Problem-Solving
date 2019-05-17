# pylint: disable=invalid-name, multiple-statements, fixme, missing-docstring, bad-indentation
def main():
    from sys import stdout
    n, t = map(int, input().split(' '))
    for _ in range(n):
        ret = solve(t)

    w = stdout.write()
    w('%d\n' % solve(t))

def solve(t):
    pass

main()
