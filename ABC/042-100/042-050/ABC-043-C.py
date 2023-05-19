# ABC-043 C - いっしょ
# https://atcoder.jp/contests/abc043/tasks/arc059_a
#
import math


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getCost(data, i):
    c = 0
    for d in data:
        c += pow(d - i, 2)
    return c


def main():
    param = getInt()

    if (param > 0):
        data = getIntList()
        ave = sum(data) / len(data)
        cost = 0
        if ave.is_integer():
            cost = getCost(data, int(ave))
        else:
            c1 = getCost(data, math.floor(ave))
            c2 = getCost(data, math.ceil(ave))
            cost = c1 if c1 < c2 else c2
        print(cost)

    else:
        print(0)


if __name__ == "__main__":
    main()
