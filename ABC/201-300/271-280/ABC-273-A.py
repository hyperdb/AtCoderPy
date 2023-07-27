# ABC-273 A - A Recursive Function
# https://atcoder.jp/contests/abc273/tasks/abc273_a
#
def getInt():
    return int(input())


def r(x):
    return 1 if x == 0 else x * r(x - 1)


def main():
    n = getInt()

    print(r(n))


if __name__ == "__main__":
    main()
