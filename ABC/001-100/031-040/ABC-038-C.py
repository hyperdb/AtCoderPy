# ABC-038 C - 単調増加
# https://atcoder.jp/contests/abc038/tasks/abc038_c
#
import math


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    b = []
    for i in range(1, N):
        if a[i] <= a[i - 1]:
            b.append(i)
    b.append(N)

    b = [0] + b
    r = 0
    for i in range(1, len(b)):
        c = b[i] - b[i - 1]
        r += c
        r += math.comb(c, 2)
    print(r)


if __name__ == "__main__":
    main()
