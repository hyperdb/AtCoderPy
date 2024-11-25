# ABC-379 A - Cyclic
# https://atcoder.jp/contests/abc379/tasks/abc379_a
#
def getInt():
    return int(input())


def shiftL(n):
    d, m = divmod(n, 100)
    return m * 10 + d


def main():
    N = getInt()

    a = shiftL(N)

    print(a, shiftL(a))


if __name__ == "__main__":
    main()
