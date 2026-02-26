# ABC-088 C - Takahashi's Information
# https://atcoder.jp/contests/abc088/tasks/abc088_c
#
def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


# 行や列の差分が全て同じかを確認する関数
def check_diff(diff_array):
    for row in diff_array:
        if len(set(row)) != 1:
            return False
    return True


def main():
    c = getIntListRow(3)

    # a1 + b1 | a1 + b2 | a1 + b3
    # a2 + b1 | a2 + b2 | a2 + b3
    # a3 + b1 | a3 + b2 | a3 + b3
    #
    # 行の差分は a2 - a1, a3 - a2
    # 列の差分は b2 - b1, b3 - b2
    #
    # 差分を取ると行の例は以下のようになる。
    # a2 - a1 | a2 - a1 | a2 - a1
    # a3 - a2 | a3 - a2 | a3 - a2
    #
    # 行の差分と列の差分が全て同じであれば、Yes となる。

    # 行の差分を求める
    row_diff = []
    for i in range(1, 3):
        row_diff.append([c[i][j] - c[i - 1][j] for j in range(3)])
    # 行の差分が全て同じかを確認
    result = check_diff(row_diff)

    if not result:
        print("No")
        return

    # 列の差分を求める
    col_diff = []
    for j in range(1, 3):
        col_diff.append([c[i][j] - c[i][j - 1] for i in range(3)])

    # 列の差分が全て同じかを確認
    result = check_diff(col_diff)
    if not result:
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
