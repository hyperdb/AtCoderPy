# ABC-091 A - Two Coins
# https://atcoder.jp/contests/abc091/tasks/abc091_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print('Yes' if a + b >= c else 'No')


if __name__ == "__main__":
    main()
