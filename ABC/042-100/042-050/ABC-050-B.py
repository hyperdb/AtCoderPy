# ABC-050 B - Contest with Drinks Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def adjust(t, d):
    c = d[0]
    return d[1] - t[c - 1]


def main():
    n = getInt()
    t = getIntList()
    m = getInt()
    data = getIntListRow(m)

    for d in data:
        s = sum(t)
        print(s + adjust(t, d))


if __name__ == "__main__":
    main()
