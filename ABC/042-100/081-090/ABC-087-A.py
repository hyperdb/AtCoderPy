# ABC-087 A - Buying Sweets
# https://atcoder.jp/contests/abc087/tasks/abc087_a
#
def getInt():
    return int(input())


def main():
    x = getInt()
    a = getInt()
    b = getInt()

    print((x - a) % b)


if __name__ == "__main__":
    main()
