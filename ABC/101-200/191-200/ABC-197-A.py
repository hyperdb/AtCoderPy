# ABC-197 A - Rotate
# https://atcoder.jp/contests/abc197/tasks/abc197_a
#
def getString():
    return input()


def main():
    s = getString()

    s += s[0]

    print(s[1:])


if __name__ == "__main__":
    main()
