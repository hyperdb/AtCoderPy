# ABC-185 B - Smartphone Addiction
# https://atcoder.jp/contests/abc185/tasks/abc185_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m, t = getIntMap()
    l = getIntListRow(m)

    s = 0
    c = n
    r = True
    for a, b in l:
        c -= (a - s)
        if c <= 0:
            r = False
            break
        c = min(c + b - a, n)
        s = b

    c -= (t - s)
    if c <= 0:
        r = False

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
