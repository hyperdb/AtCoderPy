# ABC-189 B - Alcoholic
# https://atcoder.jp/contests/abc189/tasks/abc189_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, x = getIntMap()
    l = getIntListRow(n)

    a = [v * p for v, p in l]

    s = 0
    c = 0
    r = -1
    for b in a:
        s += b
        c += 1
        if s / 100 > x:
            r = c
            break
    print(r)


if __name__ == "__main__":
    main()
