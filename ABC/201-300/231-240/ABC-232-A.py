# ABC-232 A - QQ solver
# https://atcoder.jp/contests/abc232/tasks/abc232_a
#
def getString():
    return input()


def main():
    s = getString()
    n = s.split('x')

    print(int(n[0]) * int(n[1]))


if __name__ == "__main__":
    main()
