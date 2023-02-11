# ABC-124 A - Buttons
# https://atcoder.jp/contests/abc124/tasks/abc124_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(max([a + b, a * 2 -1, b * 2 - 1]))


if __name__ == "__main__":
    main()