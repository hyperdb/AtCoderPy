# ABC-034 A - テスト
# https://atcoder.jp/contests/abc034/tasks/abc034_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    print("Better" if y > x else "Worse")


if __name__ == "__main__":
    main()
