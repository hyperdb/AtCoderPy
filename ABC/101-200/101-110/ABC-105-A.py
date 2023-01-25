# ABC-105 A - AtCoder Crackers
# https://atcoder.jp/contests/abc105/tasks/abc105_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    n, k = getIntMap()

    m = n % k

    print(0 if m == 0 else math.ceil(m / k))


if __name__ == "__main__":
    main()
