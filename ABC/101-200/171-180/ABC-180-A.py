# ABC-180 A - box
# https://atcoder.jp/contests/abc180/tasks/abc180_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, b = getIntMap()

    print(n - a + b)


if __name__ == "__main__":
    main()
