# ABC-230 B - Triple Metre
# https://atcoder.jp/contests/abc230/tasks/abc230_b
#
def getString():
    return input()


def main():
    s = getString()
    t = "oxx" * 5

    print('Yes' if s in t else 'No')


if __name__ == "__main__":
    main()
