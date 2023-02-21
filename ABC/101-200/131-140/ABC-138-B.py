# ABC-138 B - Resistors in Parallel
# https://atcoder.jp/contests/abc138/tasks/abc138_b
#
import math


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def lcm(l):
    x = l[0]
    for i in range(1, len(l)):
        x = int((x * l[i]) / math.gcd(x, l[i]))
    return x


def main():
    n = getInt()
    a = getIntList()

    m = lcm(a)

    b = 0
    for i in a:
        b += m // i

    print(m / b)


if __name__ == "__main__":
    main()
