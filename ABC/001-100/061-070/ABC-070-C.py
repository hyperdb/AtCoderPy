# ABC-070 C - Multiple Clocks
# https://atcoder.jp/contests/abc070/tasks/abc070_c
#
import math


def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def lcm(a, b):  # 最小公倍数を求める
    return (a * b) // math.gcd(a, b)


def main():
    n = getInt()
    t = getIntRow(n)

    s = t.pop(0)
    for i in t:
        s = lcm(s, i)
    print(s)


if __name__ == "__main__":
    main()
