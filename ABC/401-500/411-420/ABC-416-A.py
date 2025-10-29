# ABC-416 A - Vacation Validation
# https://atcoder.jp/contests/abc416/tasks/abc416_a
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, L, R = getIntMap()
    S = getString()

    print("Yes" if S[L - 1 : R] == "o" * (R - L + 1) else "No")


if __name__ == "__main__":
    main()
