# ABC-173 A - Payment
# https://atcoder.jp/contests/abc173/tasks/abc173_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    m = n % 1000

    print(0 if m == 0 else 1000 - m)


if __name__ == "__main__":
    main()
