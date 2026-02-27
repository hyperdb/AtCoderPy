# ABC-046 B - AtCoDeerくんとボール色塗り
# https://atcoder.jp/contests/abc046/tasks/abc046_b
#
def getIntMap() -> tuple[int, int]:
    return tuple(map(int, input().split()))


def main():
    N, K = getIntMap()

    if N == 1:
        print(K)
    else:
        print(K * ((K - 1) ** (N - 1)))


if __name__ == "__main__":
    main()
