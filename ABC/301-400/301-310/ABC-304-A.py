# ABC-304 A - First Player
# https://atcoder.jp/contests/abc304/tasks/abc304_a
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    n = getInt()
    sa = getStringListRow(n)

    s = []
    a = []
    for x, y in sa:
        s.append(x)
        a.append(int(y))

    p = a.index(min(a))

    s = s[p:] + s[0:p]

    for t in s:
        print(t)


if __name__ == "__main__":
    main()
