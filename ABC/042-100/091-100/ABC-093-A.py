# ABC-093 A - abc of ABC
# https://atcoder.jp/contests/abc093/tasks/abc093_a
#
def getString():
    return input()


def main():
    s = list(getString())
    s.sort()

    print('Yes' if ''.join(s) == 'abc' else 'No')


if __name__ == "__main__":
    main()
