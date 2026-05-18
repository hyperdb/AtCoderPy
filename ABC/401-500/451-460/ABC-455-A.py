# ABC-455 A - 455
# https://atcoder.jp/contests/abc455/tasks/abc455_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C = getIntMap()

    print("Yes" if A != B and B == C else "No")


if __name__ == "__main__":
    main()
