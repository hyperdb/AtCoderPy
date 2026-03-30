# ABC-449 A - π
# https://atcoder.jp/contests/abc449/tasks/abc449_a
#
import math


def getInt():
    return int(input())


def main():
    D = getInt()
    # 半径✕半径✕円周率
    print((D / 2) ** 2 * math.pi)


if __name__ == "__main__":
    main()
