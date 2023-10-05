# ABC-320 A - Leyland Number
# https://atcoder.jp/contests/abc320/tasks/abc320_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a ** b + b ** a)


if __name__ == "__main__":
    main()
