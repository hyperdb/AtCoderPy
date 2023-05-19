# ABC-209 A - Counting
# https://atcoder.jp/contests/abc209/tasks/abc209_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(b - a + 1 if b >= a else 0)


if __name__ == "__main__":
    main()
