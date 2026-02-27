# ABC-046 C - AtCoDeerくんと選挙速報
# https://atcoder.jp/contests/abc046/tasks/arc062_a
#
def getInt() -> int:
    return int(input())


def getIntListRow(N: int) -> list[list[int]]:
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N: int = getInt()
    TA: list[list[int]] = getIntListRow(N)

    rt: int = 1
    ra: int = 1
    for i in range(N):
        T: int = TA[i][0]
        A: int = TA[i][1]

        x: int = (rt + T - 1) // T
        y: int = (ra + A - 1) // A

        rt = T * max(x, y)
        ra = A * max(x, y)

    print(rt + ra)


if __name__ == "__main__":
    main()
