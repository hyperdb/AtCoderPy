# ABC-265 B - Explore
# https://atcoder.jp/contests/abc265/tasks/abc265_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m, t = getIntMap()
    a = [0] + getIntList()
    xy = getIntListRow(m)
    b = [0 for _ in range(n + 1)]

    for x, y in xy:
        b[x] = y

    r = True
    for i in range(2, n + 1):
        t -= a[i - 1]
        if t <= 0:
            r = False
            break
        t += b[i]

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
