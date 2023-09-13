# ABC-304 B - Subscribers
# https://atcoder.jp/contests/abc304/tasks/abc304_b
#
def getInt():
    return int(input())


def main():
    n = getInt()
    s = str(n)

    print(s[0:3] + '0' * (len(s) - 3))


if __name__ == "__main__":
    main()
