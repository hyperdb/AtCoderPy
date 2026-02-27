# ABC-092 C - Traveling Plan
# https://atcoder.jp/contests/abc092/tasks/arc093_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList() + [0]  # 出発地との往復を前後に追加する

    ## 全体のコストを計算する
    allCost = 0
    for i in range(1, len(A)):
        allCost += abs(A[i] - A[i - 1])

    ## 各点を削除したときのコストを計算する
    for i in range(1, N + 1):
        ## 前後のコストを計算する
        delCost = abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i])
        ## 1つ前と1つ後を直接つなげるコストを計算する
        addCost = abs(A[i + 1] - A[i - 1])

        ## 全体のコストから前後のコストを引き、直接つなげるコストを加える
        print(allCost - delCost + addCost)


if __name__ == "__main__":
    main()
