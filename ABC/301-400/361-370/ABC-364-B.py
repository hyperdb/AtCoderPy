# ABC-364 B - Grid Walk
# https://atcoder.jp/contests/abc364/tasks/abc364_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def getString():
    return input()


def main():
    H, W = getIntMap()
    S = getIntList()
    C = getStringListRow(H)
    X = getString()

    i = S[0] - 1
    j = S[1] - 1

    for d in X:
        if d == "U":
            if i - 1 >= 0 and C[i - 1][j] == ".":
                i -= 1
        if d == "D":
            if i + 1 < H and C[i + 1][j] == ".":
                i += 1
        if d == "L":
            if j - 1 >= 0 and C[i][j - 1] == ".":
                j -= 1
        if d == "R":
            if j + 1 < W and C[i][j + 1] == ".":
                j += 1

    print(i + 1, j + 1)


if __name__ == "__main__":
    main()
