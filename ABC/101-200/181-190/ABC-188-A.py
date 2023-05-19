# ABC-188 A - Three-Point Shot
# https://atcoder.jp/contests/abc188/tasks/abc188_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    print('Yes' if abs(x - y) < 3 else 'No')


if __name__ == "__main__":
    main()
