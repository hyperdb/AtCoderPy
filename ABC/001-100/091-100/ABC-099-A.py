# ABC-099 A - ABD
# https://atcoder.jp/contests/abc099/tasks/abc099_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print('ABD' if n // 1000 == 1 else 'ABC')


if __name__ == "__main__":
    main()
