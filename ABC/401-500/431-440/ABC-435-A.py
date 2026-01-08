# ABC-435 A - Triangular Number
# https://atcoder.jp/contests/abc435/tasks/abc435_a
#
def getInt():
    return int(input())


def main():
    N = getInt()

    print((1 + N) * N // 2)


if __name__ == "__main__":
    main()
