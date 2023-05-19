# ABC-160 A - Coffee
# https://atcoder.jp/contests/abc160/tasks/abc160_a
#
def getString():
    return input()


def main():
    s = list(getString())

    print('Yes' if s[2] == s[3] and s[4] == s[5] else 'No')


if __name__ == "__main__":
    main()
