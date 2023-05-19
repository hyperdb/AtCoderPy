# ABC-120 A - Favorite Sound
# https://atcoder.jp/contests/abc120/tasks/abc120_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    x = b // a

    print(c if c < x else x)


if __name__ == "__main__":
    main()
