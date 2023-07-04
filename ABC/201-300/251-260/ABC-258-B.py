# ABC-258 B - Number Box
# https://atcoder.jp/contests/abc258/tasks/abc258_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, list(input()))) for _ in range(N)]


def go_N(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + n - 1) % n
    return int("".join(map(str, x)))


def go_NE(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + n - 1) % n
        c = (c + 1) % n
    return int("".join(map(str, x)))


def go_E(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        c = (c + 1) % n
    return int("".join(map(str, x)))


def go_SE(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + 1) % n
        c = (c + 1) % n
    return int("".join(map(str, x)))


def go_S(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + 1) % n
    return int("".join(map(str, x)))


def go_SW(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + 1) % n
        c = (c + n - 1) % n
    return int("".join(map(str, x)))


def go_W(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        c = (c + n - 1) % n
    return int("".join(map(str, x)))


def go_NW(r, c, a):
    n = len(a)
    x = []
    for i in range(n):
        x.append(a[r][c])
        r = (r + n - 1) % n
        c = (c + n - 1) % n
    return int("".join(map(str, x)))


def main():
    n = getInt()
    a = getIntListRow(n)

    x = 0
    for r in range(n):
        for c in range(n):
            x = max(x, go_N(r, c, a))
            x = max(x, go_NE(r, c, a))
            x = max(x, go_E(r, c, a))
            x = max(x, go_SE(r, c, a))
            x = max(x, go_S(r, c, a))
            x = max(x, go_SW(r, c, a))
            x = max(x, go_W(r, c, a))
            x = max(x, go_NW(r, c, a))
    print(x)


if __name__ == "__main__":
    main()
