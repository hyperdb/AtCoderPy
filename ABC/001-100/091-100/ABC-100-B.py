# ABC-100 B - Ringo's Favorite Numbers
# https://atcoder.jp/contests/abc100/tasks/abc100_b
#
def getIntMap():
    return map(int, input().split())


def main():
    d, n = getIntMap()

    print(100 ** d * (n if n < 100 else 101))


if __name__ == "__main__":
    main()
