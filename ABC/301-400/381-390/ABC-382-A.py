# ABC-382 A - Daily Cookie
# https://atcoder.jp/contests/abc382/tasks/abc382_a
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, D = getIntMap()
    S = getString()

    print(N - (S.count("@") - D))


if __name__ == "__main__":
    main()
