# ABC-405 A - Is it rated?
# https://atcoder.jp/contests/abc405/tasks/abc405_a
#
def getIntMap():
    return map(int, input().split())


def main():
    R, X = getIntMap()

    print("Yes" if (X == 1 and 1600 <= R <= 2999) or (X == 2 and 1200 <= R <= 2399) else "No")


if __name__ == "__main__":
    main()
