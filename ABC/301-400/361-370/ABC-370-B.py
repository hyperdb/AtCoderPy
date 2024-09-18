# ABC-370 B - Binary Alchemy
# https://atcoder.jp/contests/abc370/tasks/abc370_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [[0] + list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    A = [[0]] + getIntListRow(N)

    e = 1
    for x in range(N):
        i = max(e, x + 1)
        j = min(e, x + 1)
        e = A[i][j]

    print(e)


if __name__ == "__main__":
    main()
