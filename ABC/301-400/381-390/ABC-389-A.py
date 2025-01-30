# ABC-389 A - 9x9
# https://atcoder.jp/contests/abc389/tasks/abc389_a
#
def getString():
    return input()


def main():
    S = getString()
    n = list(map(int, S.split("x")))

    print(n[0] * n[1])


if __name__ == "__main__":
    main()
