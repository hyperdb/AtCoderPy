# ABC-458 A - Chompers
# https://atcoder.jp/contests/abc458/tasks/abc458_a
#
def getString():
    return input()


def getInt():
    return int(input())


def main():
    S = getString()
    N = getInt()

    # N文字目から後ろからN文字目までを出力
    print(S[N:-N])


if __name__ == "__main__":
    main()
