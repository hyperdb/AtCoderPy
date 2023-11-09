# ABC-325 B - World Meeting
# https://atcoder.jp/contests/abc325/tasks/abc325_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    wx = getIntListRow(n)

    time_tbl = [[0 for _ in range(24)] for _ in range(n)]

    c = 0
    for w, x in wx:
        for i in range(9, 18):
            time_tbl[c][i] = w
        time_tbl[c] = time_tbl[c][x:] + time_tbl[c][:x]
        c += 1

    max_n = 0
    for i in range(24):
        num = 0
        for j in time_tbl:
            num += j[i]
        max_n = max(max_n, num)

    print(max_n)


if __name__ == "__main__":
    main()
