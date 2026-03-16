# ABC-448 B - Pepper Addiction
# https://atcoder.jp/contests/abc448/tasks/abc448_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    C = [0] + getIntList()
    AB = getIntListRow(N)

    # コショウの使用量を保存する配列
    D = [0] * (M + 1)
    # コショウの量を順番に見ていく
    for A, B in AB:
        # 最大量を超えないように、D[A]を更新する
        D[A] = min(D[A] + B, C[A])

    print(sum(D))


if __name__ == "__main__":
    main()
