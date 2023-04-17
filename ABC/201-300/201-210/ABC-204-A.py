# ABC-204 A - Rock-paper-scissors
# https://atcoder.jp/contests/abc204/tasks/abc204_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    print(x if x == y else 3 - (x + y))


if __name__ == "__main__":
    main()
