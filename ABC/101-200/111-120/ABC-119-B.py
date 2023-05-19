# ABC-119 B - Digital Gifts
# https://atcoder.jp/contests/abc119/tasks/abc119_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def yen(a):
    x, u = a

    return float(x) if u == 'JPY' else 380000.0 * float(x)


def main():
    n = getInt()
    d = getStringListRow(n)

    r = 0.0
    for a in d:
        r += yen(a)
    print(r)


if __name__ == "__main__":
    main()
