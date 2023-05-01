# ABC-126 A - Signed Difficulty
# https://atcoder.jp/contests/abc216/tasks/abc216_a
#
def getString():
    return input()


def main():
    x, y = getString().split('.')

    print('%s%s' % (x, '-' if y <= '2' else '+' if y >= '7' else ''))


if __name__ == "__main__":
    main()
