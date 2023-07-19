# ABC-268 B - Prefix?
# https://atcoder.jp/contests/abc268/tasks/abc268_b
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    print('Yes' if t.find(s) == 0 else 'No')


if __name__ == "__main__":
    main()
