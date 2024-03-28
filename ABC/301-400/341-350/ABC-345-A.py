# ABC-345 A - Leftrightarrow
# https://atcoder.jp/contests/abc345/tasks/abc345_a
#
def getString():
    return input()


def main():
    s = getString()

    r = True
    if s[0] != '<':
        r = False
    elif s[-1] != '>':
        r = False
    elif s[1:-1] != ('=' * (len(s) - 2)):
        r = False

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
