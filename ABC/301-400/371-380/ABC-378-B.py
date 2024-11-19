# ABC-378 B - Garbage Collection
# https://atcoder.jp/contests/abc378/tasks/abc378_b
#
import math


def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    qr = getIntListRow(N)
    Q = getInt()
    td = getIntListRow(Q)

    for t, d in td:
        q, r = qr[t - 1]
        if r >= d:
            print(r)
        else:
            print(r + math.ceil((d - r) / q) * q)


if __name__ == "__main__":
    main()
