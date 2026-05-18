# ABC-454 A - Closed interval
# https://atcoder.jp/contests/abc454/tasks/abc454_a
#
def getIntMap():
    return map(int, input().split())


def main():
    L, R = getIntMap()

    print(R - L + 1)


if __name__ == "__main__":
    main()
