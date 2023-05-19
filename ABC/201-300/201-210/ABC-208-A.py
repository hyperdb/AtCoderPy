# ABC-208 A - Rolling Dice
# https://atcoder.jp/contests/abc208/tasks/abc208_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yes' if a <= b <= a * 6 else 'No')


if __name__ == "__main__":
    main()
