# ABC-151 A - Next Alphabet
# https://atcoder.jp/contests/abc151/tasks/abc151_a
#
def getString():
    return input()


def main():
    s = getString()

    print(chr(ord(s) + 1))


if __name__ == "__main__":
    main()
