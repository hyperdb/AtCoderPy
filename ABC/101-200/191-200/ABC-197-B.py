# ABC-197 B - Visibility
# https://atcoder.jp/contests/abc197/tasks/abc197_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    h, w, x, y = getIntMap()
    s = getStringRow(h)

    n = 1
    for xp in range(x, h):
        # print(y - 1, xp, s[xp][y - 1])
        if s[xp][y - 1] == '#':
            break
        n += 1
    for xp in range(x - 2, -1, -1):
        # print(y - 1, xp, s[xp][y - 1])
        if s[xp][y - 1] == '#':
            break
        n += 1
    for yp in range(y, w):
        # print(yp, x - 1, s[x - 1][yp])
        if s[x - 1][yp] == '#':
            break
        n += 1
    for yp in range(y - 2, -1, -1):
        # print(yp, x - 1, s[x - 1][yp])
        if s[x - 1][yp] == '#':
            break
        n += 1

    print(n)


if __name__ == "__main__":
    main()
