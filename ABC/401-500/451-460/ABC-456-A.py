# ABC-456 A - Dice
# https://atcoder.jp/contests/abc456/tasks/abc456_a
#
def getInt():
    return int(input())


def main():
    N = getInt()

    print("Yes" if 3 <= N <= 18 else "No")


if __name__ == "__main__":
    main()
