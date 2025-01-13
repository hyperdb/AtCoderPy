# ABC-385 A - Equally
# https://atcoder.jp/contests/abc385/tasks/abc385_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C = getIntMap()
    d = A + B + C

    if A == B == C:
        print("Yes")
    elif d == 2 * A or d == 2 * B or d == 2 * C:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
