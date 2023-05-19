# ABC-175 B - Making Triangle
# https://atcoder.jp/contests/abc175/tasks/abc175_b
#
import itertools


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    l = getIntList()

    c = 0
    a = list(itertools.combinations(l, 3))
    for t in a:
        if len(set(t)) != 3:
            continue

        x, y, z = sorted(t)
        if x + y > z:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
