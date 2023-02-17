# ABC-132 A - Fifty-Fifty
# https://atcoder.jp/contests/abc132/tasks/abc132_a
#
def getString():
    return input()


def main():
    s = list(getString())

    print('Yes' if len(set(s)) == 2 else 'No')


if __name__ == "__main__":
    main()
