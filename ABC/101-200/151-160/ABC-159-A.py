# ABC-159 A - The Number of Even Pairs
# https://atcoder.jp/contests/abc159/tasks/abc159_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    n, m = getIntMap()

    print(math.comb(n, 2) + math.comb(m, 2))


if __name__ == "__main__":
    main()
