# ABC-187 B - Gentle Pairs
# https://atcoder.jp/contests/abc187/tasks/abc187_b
#
import itertools


def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def s(x, y):
    return (y[1] - x[1]) / (y[0] - x[0])


def main():
    n = getInt()
    l = getIntListRow(n)

    c = itertools.combinations([i for i in range(n)], 2)

    r = 0
    if n > 1:
        for a, b in list(c):
            if abs(s(l[a], l[b])) <= 1:
                r += 1
    print(r)


if __name__ == "__main__":
    main()
