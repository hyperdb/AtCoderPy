# ABC-047 B - すぬけ君の塗り絵 2 イージー
# https://atcoder.jp/contests/abc047/tasks/abc047_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    w, h, n = getIntMap()
    l = getIntListRow(n)

    m = [[1 for _ in range(w)] for _ in range(h)]

    for r in l:
        if r[2] == 1:
            for i in range(h):
                for j in range(r[0]):
                    m[i][j] = 0
        elif r[2] == 2:
            for i in range(h):
                for j in range(r[0], w):
                    m[i][j] = 0

        elif r[2] == 3:
            for i in range(r[1]):
                for j in range(w):
                    m[i][j] = 0
        else:
            for i in range(r[1], h):
                for j in range(w):
                    m[i][j] = 0
    print(sum(sum(row) for row in m))


if __name__ == "__main__":
    main()
