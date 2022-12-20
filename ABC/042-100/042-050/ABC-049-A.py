# ABC-049 A - 居合を終え、青い絵を覆う
# https://atcoder.jp/contests/abc049/tasks/abc049_a
#
def getString():
    return input()


def main():
    c = getString()
    if c in ['a', 'i', 'u', 'e', 'o']:
        print('vowel')
    else:
        print('consonant')


if __name__ == "__main__":
    main()
