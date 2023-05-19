# ABC-157 A - Duplex Printing
# https://atcoder.jp/contests/abc157/tasks/abc157_a
#
import math


def getInt():
    return int(input())


def main():
    n = getInt()

    print(math.ceil(n / 2))


if __name__ == "__main__":
    main()
