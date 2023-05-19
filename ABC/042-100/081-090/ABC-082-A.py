# ABC-082 A - Round Up the Mean
# https://atcoder.jp/contests/abc082/tasks/abc082_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(math.ceil((a + b) / 2))


if __name__ == "__main__":
    main()
