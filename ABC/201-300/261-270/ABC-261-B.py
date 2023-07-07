# ABC-261 B - Tournament Result
# https://atcoder.jp/contests/abc261/tasks/abc261_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def rotate(x, n):
    b = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(x[j][i])
        b.append(t)
    return b


def main():
    n = getInt()
    a = getStringListRow(n)

    b = rotate(a, n)

    r = True
    for i in range(n):
        for j in range(i, n):
            c = a[i][j]
            d = b[i][j]
            if c == '-':
                continue
            elif c == 'D' and d == 'D':
                continue
            elif c == 'W' and d == 'L':
                continue
            elif c == 'L' and d == 'W':
                continue
            else:
                r = False
                break
    print('correct' if r else 'incorrect')


if __name__ == "__main__":
    main()
