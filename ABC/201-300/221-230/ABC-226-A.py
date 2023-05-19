# ABC-226 A - Round decimals
# https://atcoder.jp/contests/abc226/tasks/abc226_a
#
import math


def getFloat():
    return float(input())


def main():
    x = getFloat()

    print(math.floor(x + 0.5))


if __name__ == "__main__":
    main()
