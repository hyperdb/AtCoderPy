# ABC-309 A - Nine
# https://atcoder.jp/contests/abc309/tasks/abc309_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yes' if b - a == 1 and a % 3 != 0 else 'No')


if __name__ == "__main__":
    main()
