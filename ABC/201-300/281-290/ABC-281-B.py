# ABC-281 B - Sandwich Number
# https://atcoder.jp/contests/abc281/tasks/abc281_b
#
def getString():
    return input()


def main():
    s = getString()

    r = True
    if not ('A' <= s[0] <= 'Z'):
        r = False
    elif not ('A' <= s[-1] <= 'Z'):
        r = False
    elif not s[1:-1].isdigit():
        r = False
    elif len(s[1:-1]) != 6:
        r = False
    elif int(s[1:-1]) < 100000:
        r = False

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
