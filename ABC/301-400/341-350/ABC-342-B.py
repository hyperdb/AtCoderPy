# ABC-342 B - Which is ahead?
# https://atcoder.jp/contests/abc342/tasks/abc342_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    p = getIntList()
    q = getInt()
    ab = getIntListRow(q)

    for a, b in ab:
        print(a if p.index(a) < p.index(b) else b)


if __name__ == "__main__":
    main()
