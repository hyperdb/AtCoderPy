# ABC-108 A - Pair
# https://atcoder.jp/contests/abc108/tasks/abc108_a
#
def getInt():
    return int(input())


def main():
    k = getInt()

    x = k // 2
    y = k % 2

    print(x * (x + y))


if __name__ == "__main__":
    main()
