# ABC-113 A - Discount Fare
# https://atcoder.jp/contests/abc113/tasks/abc113_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    print(x + y // 2)


if __name__ == "__main__":
    main()
