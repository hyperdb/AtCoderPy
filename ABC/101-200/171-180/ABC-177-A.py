# ABC-177 A - Don't be late
# https://atcoder.jp/contests/abc177/tasks/abc177_a
#
def getIntMap():
    return map(int, input().split())


def main():
    d, t, s = getIntMap()

    print('Yes' if d / s <= t else 'No')


if __name__ == "__main__":
    main()
