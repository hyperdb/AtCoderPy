# ABC-255 A - You should output ARC, though this is ABC.
# https://atcoder.jp/contests/abc255/tasks/abc255_a
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    r, c = getIntMap()
    a = getIntListRow(2)

    print(a[r - 1][c - 1])


if __name__ == "__main__":
    main()
