# ABC-338 A - Capitalized?
# https://atcoder.jp/contests/abc338/tasks/abc338_a
#
def getString():
    return input()


def main():
    s = getString()
    t = s.capitalize()

    print('Yes' if s == t else 'No')


if __name__ == "__main__":
    main()
