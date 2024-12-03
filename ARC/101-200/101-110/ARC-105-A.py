# ARC-105 A - Fourtune Cookies
# https://atcoder.jp/contests/arc105/tasks/arc105_a
#
import itertools


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getIntList()

    total = sum(N)
    parts = []
    res = False
    for i in range(1, 4):
        parts += list(itertools.combinations(N, i))

    for p in parts:
        if sum(p) * 2 == total:
            res = True
            break

    print("Yes" if res else "No")


if __name__ == "__main__":
    main()
