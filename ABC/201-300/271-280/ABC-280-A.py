# ABC-280 A - Pawn on a Grid
# https://atcoder.jp/contests/abc280/tasks/abc280_a
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    h, w = getIntMap()
    s = getStringRow(h)

    c = 0
    for r in s:
        c += r.count('#')
    print(c)


if __name__ == "__main__":
    main()
