# ABC-336 B - CTZ
# https://atcoder.jp/contests/abc336/tasks/abc336_b
#
def getInt():
    return int(input())


def ctz(i):
    b = bin(i)[::-1]

    return b.find('1') if i > 0 else 1


def main():
    n = getInt()

    print(ctz(n))


if __name__ == "__main__":
    main()
