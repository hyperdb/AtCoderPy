# ABC-406 A - Not Acceptable
# https://atcoder.jp/contests/abc406/tasks/abc406_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C, D = getIntMap()

    print("Yes" if A * 60 + B >= C * 60 + D else "No")


if __name__ == "__main__":
    main()
