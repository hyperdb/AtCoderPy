# ABC-382 B - Daily Cookie 2
# https://atcoder.jp/contests/abc382/tasks/abc382_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, D = getIntMap()
    S = list(getString())

    S.reverse()

    for _ in range(D):
        i = S.index("@")
        S[i] = "."

    S.reverse()
    print("".join(S))


if __name__ == "__main__":
    main()
