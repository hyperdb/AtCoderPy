# ABC-463 A - 16:9
# https://atcoder.jp/contests/abc463/tasks/abc463_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y = getIntMap()

    print("Yes" if X * 9 == Y * 16 else "No")


if __name__ == "__main__":
    main()
