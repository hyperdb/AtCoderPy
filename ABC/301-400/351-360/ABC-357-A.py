# ABC-357 A - Sanitize Hands
# https://atcoder.jp/contests/abc357/tasks/abc357_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    H = getIntList()

    t = [i for i in range(N) if sum(H[: i + 1]) <= M]

    print(len(t))


if __name__ == "__main__":
    main()
