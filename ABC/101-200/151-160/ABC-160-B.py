# ABC-160 B - Golden Coins
# https://atcoder.jp/contests/abc160/tasks/abc160_b
#
def getInt():
    return int(input())


def main():
    x = getInt()

    v = x // 500 * 1000

    x %= 500

    v += x // 5 * 5

    print(v)


if __name__ == "__main__":
    main()
