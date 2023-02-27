# ABC-150 A - 500 Yen Coins
# https://atcoder.jp/contests/abc150/tasks/abc150_a
#
def getIntMap():
    return map(int, input().split())


def main():
    k, x = getIntMap()

    print('Yes' if x / k <= 500.0 else 'No')


if __name__ == "__main__":
    main()
