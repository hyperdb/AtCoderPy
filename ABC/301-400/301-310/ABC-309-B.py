# ABC-309 B - Rotate
# https://atcoder.jp/contests/abc309/tasks/abc309_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def cp(x, y):
    z = []
    for i in range(y):
        z.append([x[i][j] for j in range(y)])
    return z


def main():
    n = getInt()
    a = getStringListRow(n)
    b = cp(a, n)

    for j in range(n):
        # top
        if j == 0:
            b[j][0] = a[j + 1][0]
            for i in range(1, n):
                b[j][i] = a[j][i - 1]
        # bottom
        elif j == n - 1:
            b[j][n - 1] = a[j - 1][n - 1]
            for i in range(0, n - 1):
                b[j][i] = a[j][i + 1]
        else:
            b[j][0] = a[j + 1][0]
            b[j][n - 1] = a[j - 1][n - 1]

    for i in range(n):
        print("".join(b[i]))


if __name__ == "__main__":
    main()
