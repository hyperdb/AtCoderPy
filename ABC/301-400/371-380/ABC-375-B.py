# ABC-375 B - Traveling Takahashi Problem
# https://atcoder.jp/contests/abc375/tasks/abc375_b
#
import math


def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    XY = [[0, 0]] + getIntListRow(N) + [[0, 0]]

    d = 0.0
    for i in range(1, len(XY)):
        x1, y1 = XY[i - 1]
        x2, y2 = XY[i]

        a = math.pow(x1 - x2, 2)
        b = math.pow(y1 - y2, 2)

        d += math.pow(a + b, 0.5)

    print(d)


if __name__ == "__main__":
    main()
