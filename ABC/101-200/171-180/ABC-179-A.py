# ABC-179 A - Plural Form
# https://atcoder.jp/contests/abc179/tasks/abc179_a
#
def getString():
    return input()


def main():
    s = getString()

    print(s + ('es' if s[-1] == 's' else 's'))


if __name__ == "__main__":
    main()
