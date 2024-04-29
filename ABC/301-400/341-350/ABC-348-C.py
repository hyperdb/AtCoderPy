# ABC-348 C - Colorful Beans
# https://atcoder.jp/contests/abc348/tasks/abc348_c
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    ac = getIntListRow(n)
    m = dict()

    for a, c in ac:
        m.setdefault(c, 0)
        m[c] = a if m[c] == 0 else min(m[c], a)

    print(max(m.values()))


if __name__ == "__main__":
    main()
