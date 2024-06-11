# ABC-077 A - Rotation
# https://atcoder.jp/contests/abc077/tasks/abc077_a
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    print('YES' if s == t[::-1] else 'NO')


if __name__ == "__main__":
    main()
