# ABC-319 C - False Hope
# https://atcoder.jp/contests/abc319/tasks/abc319_c
#
import itertools
import math


def getIntList():
    return list(map(int, input().split()))


def main():
    c = getIntList() + getIntList() + getIntList()
    v = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    t = math.perm(9, 9)

    b = 0
    for x in itertools.permutations(a, 9):
        r = True
        for y in v:
            d = []
            for z in y:
                i = x.index(z)
                j = c[z]
                d.append([i, j])
            d.sort()
            if d[0][1] == d[1][1]:
                r = False
                break
        if r:
            b += 1
    print(b / t)


if __name__ == "__main__":
    main()
