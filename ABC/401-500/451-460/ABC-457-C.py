# ABC-457 C - Long Sequence
# https://atcoder.jp/contests/abc457/tasks/abc457_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, K = getIntMap()
    A = getIntListRow(N)
    C = getIntList()

    for i in range(N):
        # 配列長を取得
        L = A[i][0]
        # 配列のサイズを計算（配列長 × 繰り返し数）
        size = L * C[i]

        # K が配列のサイズ以下なら出力処理へ
        if K <= size:
            # 配列のインデックスを求めて0ベースに変換
            k = K % L - 1
            a = A[i][1:]
            # 答えを出力
            print(a[k])
            break

        # Kを配列のサイズ分減らす
        K -= size


if __name__ == "__main__":
    main()
