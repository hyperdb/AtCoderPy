# ABC-350 A - Past ABCs
# https://atcoder.jp/contests/abc350/tasks/abc350_a
#
def getString():
    return input()


def main():
    s = getString()
    q = int(s[3:])

    print('Yes' if q != 316 and 0 < q < 350 else 'No')


if __name__ == "__main__":
    main()
