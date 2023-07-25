# ABC-271 B - Maintain Multiple Sequences
# https://atcoder.jp/contests/abc271/tasks/abc271_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, q = getIntMap()
    l = getIntListRow(n)
    st = getIntListRow(q)

    for s, t in st:
        print(l[s - 1][t])


if __name__ == "__main__":
    main()
