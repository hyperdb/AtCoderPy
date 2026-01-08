# ABC-436 A - o-padding
# https://atcoder.jp/contests/abc436/tasks/abc436_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()

    T = "o" * N + S
    print(T[-1 * N :])


if __name__ == "__main__":
    main()
