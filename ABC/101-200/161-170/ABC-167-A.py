# ABC-167 A - Registration
# https://atcoder.jp/contests/abc167/tasks/abc167_a
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    print('Yes' if s == t[:-1] else 'No')


if __name__ == "__main__":
    main()
