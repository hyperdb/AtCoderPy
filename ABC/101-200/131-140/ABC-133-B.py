# ABC-133 B - Good Distance
# https://atcoder.jp/contests/abc133/tasks/abc133_b
#
import itertools
import math


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def distance(s, t):
    x = 0.0
    for i in range(len(s)):
        x += (s[i] - t[i]) ** 2
    return math.sqrt(x)


def main():
    n, d = getIntMap()
    x = getIntListRow(n)

    c = 0
    l = itertools.combinations([i for i in range(n)], 2)
    for a, b in l:
        d = distance(x[a], x[b])
        if d.is_integer():
            c += 1
    print(c)


if __name__ == "__main__":
    main()
