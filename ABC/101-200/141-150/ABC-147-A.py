# ABC-147 A - Blackjack
# https://atcoder.jp/contests/abc147/tasks/abc147_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    n = getIntList()

    print('win' if sum(n) <= 21 else 'bust')


if __name__ == "__main__":
    main()
