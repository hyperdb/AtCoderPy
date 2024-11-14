# ABC-033 B - 町の合併
# https://atcoder.jp/contests/abc033/tasks/abc033_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    N = getInt()
    SP = getStringListRow(N)

    d = dict()
    y = 0
    z = 0
    for s, p in SP:
        x = int(p)
        y = max(x, y)
        z += x

        d[x] = s

    print(d[y] if z < 2 * y else "atcoder")


if __name__ == "__main__":
    main()
