# ABC-044 A 高橋君とホテルイージー
# https://atcoder.jp/contests/abc044/tasks/abc044_a
#
def getInt() -> int:
    return int(input())


def main():
    N: int = getInt()
    K: int = getInt()
    X: int = getInt()
    Y: int = getInt()

    print((N * X) if N < K else (K * X + (N - K) * Y))


if __name__ == "__main__":
    main()
