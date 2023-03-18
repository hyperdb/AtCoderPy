# ABC-171 A - αlphabet
# https://atcoder.jp/contests/abc171/tasks/abc171_a
#
def getString():
    return input()


def main():
    s = getString()

    print('a' if ord(s) >= ord('a') else 'A')


if __name__ == "__main__":
    main()
