# ABC-418 A - I'm a teapot
# https://atcoder.jp/contests/abc418/tasks/abc418_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()

    print("Yes" if S.endswith("tea") else "No")


if __name__ == "__main__":
    main()
