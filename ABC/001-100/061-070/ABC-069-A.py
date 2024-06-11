# ABC-069 A - K-City
# https://atcoder.jp/contests/abc069/tasks/abc069_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, m = getIntMap()

    print((n - 1) * (m - 1))


if __name__ == "__main__":
    main()
