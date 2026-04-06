# ABC-451 A - illegal
# https://atcoder.jp/contests/abc451/tasks/abc451_a
#
def getString():
    return input()


def main():
    S = getString()

    print("Yes" if len(S) % 5 == 0 else "No")


if __name__ == "__main__":
    main()
