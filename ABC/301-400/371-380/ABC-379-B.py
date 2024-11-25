# ABC-379 B - Strawberries
# https://atcoder.jp/contests/abc379/tasks/abc379_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, K = getIntMap()
    S = getString()

    print(S.count("O" * K))


if __name__ == "__main__":
    main()
