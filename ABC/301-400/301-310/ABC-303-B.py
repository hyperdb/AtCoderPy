# ABC-303 B - Discord
# https://atcoder.jp/contests/abc303/tasks/abc303_b
#
import math


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    a = getIntListRow(m)
    c = []

    for b in a:
        for i in range(1, n):
            p1 = b[i - 1]
            p2 = b[i]

            x = [p1, p2]
            x.sort()

            if not x in c:
                c.append(x)

    print(math.comb(n, 2) - len(c))


if __name__ == "__main__":
    main()
