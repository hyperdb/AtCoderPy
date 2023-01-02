# ABC-073 B - Theater
# https://atcoder.jp/contests/abc073/tasks/abc073_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    d = getIntListRow(n)

    r = 0
    for i in range(n):
        r += (d[i][1] - d[i][0] + 1)
    print(r)


if __name__ == "__main__":
    main()
