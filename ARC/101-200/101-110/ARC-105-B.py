# ARC-105 B - MAX-=min
# https://atcoder.jp/contests/arc105/tasks/arc105_b
#
import math


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    x = a[0]
    for i in range(1, N):
        x = math.gcd(x, a[i])
    print(x)


if __name__ == "__main__":
    main()
