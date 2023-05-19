# ABC-086 B - 1 21
# https://atcoder.jp/contests/abc086/tasks/abc086_b
#
import math


def getStringMap():
    return input().split()


def main():
    a, b = getStringMap()

    n = int(a + b)

    print('Yes' if (math.sqrt(n)).is_integer() else 'No')


if __name__ == "__main__":
    main()
