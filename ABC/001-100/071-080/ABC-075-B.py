# ABC-075 B - Minesweeper
# https://atcoder.jp/contests/abc075/tasks/abc075_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def check(x, y, h, w, s):
    a = x - 1
    b = y - 1

    c = 0
    for i in range(3):
        for j in range(3):
            if a + i >= 0 and a + i < h and b + j >= 0 and b + j < w:
                if s[a + i][b + j] == '#':
                    c += 1
    return str(c)


def main():
    h, w = getIntMap()
    s = getStringListRow(h)

    for x in range(h):
        for y in range(w):
            if s[x][y] == '#':
                continue
            s[x][y] = check(x, y, h, w, s)
        print("".join(s[x]))


if __name__ == "__main__":
    main()
