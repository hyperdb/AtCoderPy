# ABC-088 A - Infinite Coins
# https://atcoder.jp/contests/abc088/tasks/abc088_a
#
def getInt():
    return int(input())


def main():
    n = getInt()
    a = getInt()

    print('Yes' if (n % 500) <= a else 'No')


if __name__ == "__main__":
    main()
