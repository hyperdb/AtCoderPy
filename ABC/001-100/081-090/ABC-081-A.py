# ABC-081 A - Placing Marbles
# https://atcoder.jp/contests/abc081/tasks/abc081_a
#
def getString():
    return input()


def main():
    s = list(map(int, list(getString())))

    print(sum(s))


if __name__ == "__main__":
    main()
