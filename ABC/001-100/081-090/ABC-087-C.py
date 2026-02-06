# ABC-087 C - Candies
# https://atcoder.jp/contests/abc087/tasks/arc090_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    A = getIntListRow(2)

    max_sum = 0
    for i in range(N):
        # 上列の合計を計算
        upper = sum(A[0][:i])
        # 下列の合計を計算
        lower = sum(A[1][i + 1 :])
        # 交差部分を計算
        cross = A[0][i] + A[1][i]

        max_sum = max(max_sum, upper + lower + cross)

    print(max_sum)


if __name__ == "__main__":
    main()
