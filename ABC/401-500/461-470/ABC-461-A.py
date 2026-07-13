# ABC-461 A - Armor
# https://atcoder.jp/contests/abc461/tasks/abc461_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, D = getIntMap()

    print("Yes" if A <= D else "No")


if __name__ == "__main__":
    main()
