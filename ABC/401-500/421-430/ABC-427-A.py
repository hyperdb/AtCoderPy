# ABC-427 A - ABC -> AC
# https://atcoder.jp/contests/abc427/tasks/abc427_a
#
def getString():
    return input()


def main():
    S = getString()
    m = len(S) // 2

    print(S[:m] + S[m + 1 :])


if __name__ == "__main__":
    main()
