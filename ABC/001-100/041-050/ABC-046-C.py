# ABC-046 C - AtCoDeerくんと選挙速報
# https://atcoder.jp/contests/abc046/tasks/arc062_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    TA = getIntListRow(N)

    rt = 1
    ra = 1
    for i in range(N):
        T = TA[i][0]
        A = TA[i][1]

        x = (rt + T - 1) // T
        y = (ra + A - 1) // A

        rt = T * max(x, y)
        ra = A * max(x, y)

    print(rt + ra)


if __name__ == "__main__":
    main()
