# ABC-152 A - AC or WA
# https://atcoder.jp/contests/abc152/tasks/abc152_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, m = getIntMap()

    print('Yes' if n == m else 'No')


if __name__ == "__main__":
    main()
