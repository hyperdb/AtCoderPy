# ABC-368 A - Cut
# https://atcoder.jp/contests/abc368/tasks/abc368_a
#
def getIntMap():
    return map(int, input().split())


def getStringList():
    return list(input().split())


def main():
    N, K = getIntMap()
    A = getStringList()

    print(" ".join((A[(-1 * K) :] + A[: (N - K)])))


if __name__ == "__main__":
    main()
