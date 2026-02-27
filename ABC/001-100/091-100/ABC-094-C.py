# ABC-094 C - Many Medians
# https://atcoder.jp/contests/abc094/tasks/arc095_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    X = getIntList()
    A = sorted(X)

    # 中央値を求める
    center = N // 2 - 1
    # 中央値は偶数個のときは2つある
    m1 = A[center]
    m2 = A[center + 1]

    # 除外する数を順番に処理する
    for n in range(N):
        remove = X[n]
        # 除外する数がm1以下(前半)ならm2
        if remove <= m1:
            print(m2)
        # そうでなければm1
        else:
            print(m1)


if __name__ == "__main__":
    main()
