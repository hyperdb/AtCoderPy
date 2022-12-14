# ABC-044 A 高橋君とホテルイージー
# https://atcoder.jp/contests/abc044/tasks/abc044_a
#
def getInt():
    return int(input())


def main():
    N = getInt()
    K = getInt()
    X = getInt()
    Y = getInt()

    if (N < K):
        print(N * X)
    else:
        print(K * X + (N - K) * Y)


if __name__ == "__main__":
    main()
