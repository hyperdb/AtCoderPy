# ABC-417 A - A Substring
# https://atcoder.jp/contests/abc417/tasks/abc417_a
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, A, B = getIntMap()
    S = getString()

    if A == B == 0:
        print(S)
    elif A == 0 and B > 0:
        print(S[: N - B])
    elif A > 0 and B == 0:
        print(S[A:])
    else:
        print(S[A : N - B])


if __name__ == "__main__":
    main()
