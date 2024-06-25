# ABC-358 A - Welcome to AtCoder Land
# https://atcoder.jp/contests/abc358/tasks/abc358_a
#
def getStringMap():
    return input().split()


def main():
    S, T = getStringMap()

    print('Yes' if S == 'AtCoder' and T == 'Land' else 'No')


if __name__ == "__main__":
    main()
