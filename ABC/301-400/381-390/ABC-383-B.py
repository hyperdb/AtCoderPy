# ABC-383 B - Humidifier 2
# https://atcoder.jp/contests/abc383/tasks/abc383_b
#
import itertools


def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    H, W, D = getIntMap()
    S = getStringRow(H)

    n = []  # 床

    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                n.append([h, w])

    fc = len(n)
    d = [set() for _ in range(fc)]
    for i in range(fc):
        x1, y1 = n[i]
        for x2, y2 in n:
            mn = abs(x1 - x2) + abs(y1 - y2)
            if mn <= D:
                d[i].add((x2, y2))

    c = itertools.combinations([i for i in range(fc)], 2)

    r = 0
    for p1, p2 in c:
        r = max(r, len(d[p1] | d[p2]))
    print(r)


if __name__ == "__main__":
    main()
