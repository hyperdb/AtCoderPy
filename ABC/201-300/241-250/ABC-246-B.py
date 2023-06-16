# ABC-246 B - Get Closer
# https://atcoder.jp/contests/abc246/tasks/abc246_b
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = math.sqrt(a ** 2 + b ** 2)

    print(a / c, b / c)


if __name__ == "__main__":
    main()
