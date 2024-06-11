# ABC-055 A - Restaurant
# https://atcoder.jp/contests/abc055/tasks/abc055_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print((n * 800) - ((n // 15) * 200))


if __name__ == "__main__":
    main()
