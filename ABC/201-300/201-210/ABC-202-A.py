# ABC-202 A - Three Dice
# https://atcoder.jp/contests/abc202/tasks/abc202_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print(21 - sum([a, b, c]))


if __name__ == "__main__":
    main()
