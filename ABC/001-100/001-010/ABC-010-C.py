# ABC-010 C - 浮気調査
# https://atcoder.jp/contests/abc010/tasks/abc010_3
#
import math


def getIntMap():
    return map(int, input().split())


def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def main():
    sx, sy, ex, ey, T, V = getIntMap()
    n = getInt()
    xy = getIntListRow(n)

    r = False
    for x, y in xy:
        ra = distance(x, y, sx, sy)
        rb = distance(x, y, ex, ey)

        if float(T * V) >= (ra + rb):
            r = True
            break

    print('YES' if r else 'NO')


if __name__ == "__main__":
    main()
