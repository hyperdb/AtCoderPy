# ABC-220 B - Base K
# https://atcoder.jp/contests/abc220/tasks/abc220_b
#
def getInt():
    return int(input())


def getStringMap():
    return input().split()


def main():
    k = getInt()
    a, b = getStringMap()

    print(int(a, k) * int(b, k))


if __name__ == "__main__":
    main()
