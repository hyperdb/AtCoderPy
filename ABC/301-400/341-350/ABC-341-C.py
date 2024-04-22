# ABC-341 C - Takahashi Gets Lost
# https://atcoder.jp/contests/abc341/tasks/abc341_c
# CPythonではTLE、PyPyでAC
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def getStringRow(N):
    return [input() for _ in range(N)]


def check(x, y, r, m):

    if m[y][x] == '#':
        return 0

    for c in r:
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y -= 1
        elif c == 'D':
            y += 1

        if m[y][x] == '#':
            return 0

    return 1


def main():
    h, w, n = getIntMap()
    t = getString()
    s = getStringRow(h)

    c = 0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            c += check(x, y, t, s)

    print(c)


if __name__ == "__main__":
    main()
