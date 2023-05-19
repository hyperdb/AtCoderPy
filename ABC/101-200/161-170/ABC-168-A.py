# ABC-168 A - ∴ (Therefore)
# https://atcoder.jp/contests/abc168/tasks/abc168_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    n %= 10

    print('bon' if n == 3 else 'pon' if n in [0, 1, 6, 8] else 'hon')


if __name__ == "__main__":
    main()
