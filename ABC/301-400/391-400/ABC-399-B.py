# ABC-399 B - Ranking with Ties
# https://atcoder.jp/contests/abc399/tasks/abc399_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    P = getIntList()

    # count item
    r = dict()
    for x in set(P):
        r[x] = P.count(x)

    # sort desc
    s = sorted(r, key=lambda x: x)
    s.reverse()

    # position
    t = dict()
    c = 1
    for x in s:
        t[x] = c
        c += r[x]

    # output
    for x in P:
        print(t[x])


if __name__ == "__main__":
    main()
