# ABC-331 B - Buy One Carton of Milk
# https://atcoder.jp/contests/abc331/tasks/abc331_b
#
import math
import sys


def getIntMap():
    return map(int, input().split())


def count_items(i, j, k):
    return i * 6 + j * 8 + k * 12


def main():
    n, s, m, l = getIntMap()

    p = sys.maxsize
    for i in [x for x in range(math.ceil(n / 6) + 1)]:
        for j in [x for x in range(math.ceil(n / 8) + 1)]:
            for k in [x for x in range(math.ceil(n / 12) + 1)]:
                if count_items(i, j, k) < n:
                    continue
                p = min(p, i * s + j * m + k * l)
    print(p)


if __name__ == "__main__":
    main()
