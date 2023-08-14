# ABC-283 B - First Query Problem
# https://atcoder.jp/contests/abc283/tasks/abc283_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    a = [0] + getIntList()
    q = getInt()
    qt = getIntListRow(q)

    for qs in qt:
        if qs[0] == 1:
            a[qs[1]] = qs[2]
        elif qs[0] == 2:
            print(a[qs[1]])


if __name__ == "__main__":
    main()
