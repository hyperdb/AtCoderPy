# ABC-186 A - Brick
# https://atcoder.jp/contests/abc186/tasks/abc186_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, w = getIntMap()

    print(n // w)


if __name__ == "__main__":
    main()
