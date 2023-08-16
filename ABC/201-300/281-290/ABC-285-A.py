# ABC-285 A - Edge Checker 2
# https://atcoder.jp/contests/abc285/tasks/abc285_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yes' if b // 2 == a else 'No')


if __name__ == "__main__":
    main()
