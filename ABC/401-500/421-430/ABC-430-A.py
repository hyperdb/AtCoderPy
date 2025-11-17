# ABC-430 A - Candy Cookie Law
# https://atcoder.jp/contests/abc430/tasks/abc430_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C, D = getIntMap()

    print("Yes" if A <= C and B > D else "No")


if __name__ == "__main__":
    main()
