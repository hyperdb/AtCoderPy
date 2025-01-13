# ABC-385 B - Santa Claus 1
# https://atcoder.jp/contests/abc385/tasks/abc385_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def getString():
    return input()


def main():
    H, W, X, Y = getIntMap()
    S = getStringRow(H)
    T = list(getString())

    x = X - 1
    y = Y - 1

    r = 0
    for c in T:
        if c == "U":
            if x == 0:
                continue
            if S[x - 1][y] == "#":
                continue
            x -= 1
        elif c == "D":
            if x == H - 1:
                continue
            if S[x + 1][y] == "#":
                continue
            x += 1
        elif c == "L":
            if y == 0:
                continue
            if S[x][y - 1] == "#":
                continue
            y -= 1
        elif c == "R":
            if y == W - 1:
                continue
            if S[x][y + 1] == "#":
                continue
            y += 1
        if S[x][y] == "@":
            r += 1
            S[x][y] = "."

    print(x + 1, y + 1, r)


if __name__ == "__main__":
    main()
