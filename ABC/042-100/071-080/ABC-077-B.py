# ABC-077 B - Around Square
# https://atcoder.jp/contests/abc077/tasks/abc077_b
#
import math


def getInt():
    return int(input())


def main():
    n = getInt()
    m = int(math.sqrt(n))
    print(m ** 2)


if __name__ == "__main__":
    main()
