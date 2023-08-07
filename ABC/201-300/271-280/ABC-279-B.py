# ABC-279 B - LOOKUP
# https://atcoder.jp/contests/abc279/tasks/abc279_b
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    print('Yes' if s.find(t) >= 0 else 'No')


if __name__ == "__main__":
    main()
