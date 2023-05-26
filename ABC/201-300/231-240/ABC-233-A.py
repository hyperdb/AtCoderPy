# ABC-233 A - 10yen Stamp
# https://atcoder.jp/contests/abc233/tasks/abc233_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    print(0 if y <= x else math.ceil((y - x) / 10))


if __name__ == "__main__":
    main()
