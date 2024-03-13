# ABC-337 A - Scoreboard
# https://atcoder.jp/contests/abc337/tasks/abc337_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    xy = getIntListRow(n)

    z = 0
    for x, y in xy:
        z += (x - y)

    print('Draw' if z == 0 else 'Takahashi' if z > 0 else 'Aoki')


if __name__ == "__main__":
    main()
