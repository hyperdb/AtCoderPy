# ABC-404 B - Grid Rotation
# https://atcoder.jp/contests/abc404/tasks/abc404_b
#
import copy


def getInt():
    return int(input())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def rotate_r(array):
    array.reverse()
    a1 = list(zip(*array, strict=False))
    a2 = list(map(list, a1))
    return a2


def diff(n, s, t):
    d = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                d += 1
    return d


def main():
    N = getInt()
    S = getStringRow(N)
    T = getStringRow(N)

    r = N**2 + 4
    for i in range(4):
        s = copy.deepcopy(S)
        if i > 0:
            for _ in range(i):
                s = rotate_r(s)

        d = diff(N, s, T)

        r = min(r, d + i)

    print(r)


if __name__ == "__main__":
    main()
