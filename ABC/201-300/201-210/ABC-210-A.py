# ABC-210 A - Cabbages
# https://atcoder.jp/contests/abc210/tasks/abc210_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, x, y = getIntMap()

    print(min(a, n) * x + max(n - a, 0) * y)


if __name__ == "__main__":
    main()
