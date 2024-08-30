# ABC-367 A - Shout Everyday
# https://atcoder.jp/contests/abc367/tasks/abc367_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C = getIntMap()

    A = A - B if A > B else A - B + 24
    C = C - B if C > B else C - B + 24

    print("No" if A < C else "Yes")


if __name__ == "__main__":
    main()
