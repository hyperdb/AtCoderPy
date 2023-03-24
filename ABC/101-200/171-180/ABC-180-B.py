# ABC-180 B - Various distances
# https://atcoder.jp/contests/abc180/tasks/abc180_b
#
import math


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def m(l):
    s = 0
    for i in l:
        s += abs(i)
    return s


def e(l):
    s = 0
    for i in l:
        s += abs(i) ** 2
    return math.sqrt(s)


def c(l):
    return max(map(abs, l))


def main():
    n = getInt()
    x = getIntList()

    print(m(x))
    print(e(x))
    print(c(x))


if __name__ == "__main__":
    main()
