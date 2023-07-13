# ABC-265 A - Apple
# https://atcoder.jp/contests/abc265/tasks/abc265_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y, n = getIntMap()

    if y < x * 3:
        s = n // 3 * y + n % 3 * x
    else:
        s = n * x

    print(s)


if __name__ == "__main__":
    main()
