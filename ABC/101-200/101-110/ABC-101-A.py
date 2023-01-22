# ABC-101 A - Eating Symbols Easy
# https://atcoder.jp/contests/abc101/tasks/abc101_a
#
def getString():
    return input()


def main():
    s = list(getString())

    c = sum([1 if t == '+' else -1 for t in s])

    print(c)


if __name__ == "__main__":
    main()
