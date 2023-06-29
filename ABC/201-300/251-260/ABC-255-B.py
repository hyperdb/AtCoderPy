# ABC-255 B - Light It Up
# https://atcoder.jp/contests/abc255/tasks/abc255_b
#
import math


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, k = getIntMap()
    a = getIntList()
    xy = getIntListRow(n)

    s = [xy[i - 1] for i in a]
    e = [xy[i] for i in range(len(xy)) if i + 1 not in a]

    r = []
    for ex, ey in e:
        p = []
        for sx, sy in s:
            d = math.sqrt((sx - ex) ** 2 + (sy - ey) ** 2)
            p.append(d)
        r.append(min(p))
    print(max(r))


if __name__ == "__main__":
    main()
