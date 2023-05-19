# ABC-065 A - Expired?
# https://atcoder.jp/contests/abc065/tasks/abc065_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, a, b = getIntMap()

    print('delicious' if b - a <= 0 else 'dangerous' if b - a > x else 'safe')


if __name__ == "__main__":
    main()
