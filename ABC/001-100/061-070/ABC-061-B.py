# ABC-061 B - Counting Roads
# https://atcoder.jp/contests/abc061/tasks/abc061_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    ab = getIntListRow(m)
    c = []
    for i in range(0, n + 1):
        c.append(0)
    for x in ab:
        for y in x:
            c[y] += 1
    for i in range(1, n + 1):
        print(c[i])


if __name__ == "__main__":
    main()
