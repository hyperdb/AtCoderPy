# ABC-200 A - Century
# https://atcoder.jp/contests/abc200/tasks/abc200_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print((n - 1) // 100 + 1)


if __name__ == "__main__":
    main()
