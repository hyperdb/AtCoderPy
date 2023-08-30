# ABC-295 B - Bombs
# https://atcoder.jp/contests/abc295/tasks/abc295_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def explode(a, x, y, w, h):
    p = int(a[y][x])

    a[y][x] = '.'

    for j in range(-p, p + 1):
        for i in range(-p, p + 1):
            if abs(i) + abs(j) > p:
                continue
            bx = x + i
            by = y + j

            if 0 <= bx < w and 0 <= by < h:
                if not a[by][bx].isdigit():
                    a[by][bx] = '.'

    return a


def main():
    r, c = getIntMap()
    b = getStringListRow(r)

    for j in range(r):
        for i in range(c):
            if b[j][i].isdigit():
                b = explode(b, i, j, c, r)

    for l in b:
        print("".join(l))


if __name__ == "__main__":
    main()
