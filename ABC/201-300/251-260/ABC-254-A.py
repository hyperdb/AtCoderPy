# ABC-254 A - Last Two Digits
# https://atcoder.jp/contests/abc254/tasks/abc254_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print('%02d' % (n % 100))


if __name__ == "__main__":
    main()
