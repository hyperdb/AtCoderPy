# ABC-176 A - Takoyaki
# https://atcoder.jp/contests/abc176/tasks/abc176_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    n, x, t = getIntMap()

    print(math.ceil(n / x) * t)


if __name__ == "__main__":
    main()
