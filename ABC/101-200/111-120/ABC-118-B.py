# ABC-118 B - Foods Loved by Everyone
# https://atcoder.jp/contests/abc118/tasks/abc118_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    x = getIntListRow(n)

    l = [0 for i in range(m + 1)]

    for y in x:
        for i in range(1, len(y)):
            l[y[i]] += 1

    c = 0
    for z in range(1, len(l)):
        if l[z] == n:
            c += 1

    print(c)


if __name__ == "__main__":
    main()
