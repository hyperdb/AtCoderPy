# ABC-258 A - When?
# https://atcoder.jp/contests/abc258/tasks/abc258_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    m = n % 60
    h = 21 + n // 60

    print('%02d:%02d' % (h, m))


if __name__ == "__main__":
    main()
