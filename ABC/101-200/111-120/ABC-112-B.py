# ABC-112 B - Time Limit Exceeded
# https://atcoder.jp/contests/abc112/tasks/abc112_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, t = getIntMap()
    l = getIntListRow(n)

    r = []
    for a, b in l:
        if b <= t:
            r.append([a, b])
    r.sort()

    print('TLE' if len(r) == 0 else r[0][0])


if __name__ == "__main__":
    main()
