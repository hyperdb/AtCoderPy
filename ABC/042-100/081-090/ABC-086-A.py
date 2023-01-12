# ABC-086 A - Product
# https://atcoder.jp/contests/abc086/tasks/abc086_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Even' if a % 2 == 0 or b % 2 == 0 else 'Odd')


if __name__ == "__main__":
    main()
