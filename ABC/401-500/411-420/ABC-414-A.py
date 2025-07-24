# ABC-414 A - Streamer Takahashi
# https://atcoder.jp/contests/abc414/tasks/abc414_a
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, L, R = getIntMap()
    XY = getIntListRow(N)

    count = 0
    for x, y in XY:
        if x <= L and y >= R:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
