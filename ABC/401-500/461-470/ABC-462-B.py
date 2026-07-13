# ABC-462 B - Gift
# https://atcoder.jp/contests/abc462/tasks/abc462_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    # 0を入れることで、1-indexedにする
    A = [[]] + getIntListRow(N)
    # 誰にもらったかを格納
    B = [[] for _ in range(N + 1)]

    # プレゼントした人をもらった人のリストに追加する
    for i in range(1, N + 1):
        for p in A[i][1:]:
            B[p].append(i)

    # 誰にもらったかのリストを出力する
    for b in B[1:]:
        # 個数と、もらった人の番号をアンパックして出力する
        print(len(b), *b)


if __name__ == "__main__":
    main()
