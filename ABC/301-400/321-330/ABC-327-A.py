# ABC-327 A - ab
# https://atcoder.jp/contests/abc327/tasks/abc327_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print('Yes' if 'ab' in s or 'ba' in s else 'No')


if __name__ == "__main__":
    main()
