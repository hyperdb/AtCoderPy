# ABC-459 A - Hell, World!
# https://atcoder.jp/contests/abc459/tasks/abc459_a
#
def getInt():
    return int(input())


def main():
    N = getInt()
    S = "HelloWorld"

    print(S[: N - 1] + S[N:])


if __name__ == "__main__":
    main()
