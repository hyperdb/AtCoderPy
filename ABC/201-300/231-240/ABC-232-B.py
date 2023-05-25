# ABC-232 B - Caesar Cipher
# https://atcoder.jp/contests/abc232/tasks/abc232_b
#
def getString():
    return input()


def diff(x, y):
    a = ord(y) - ord(x)
    return a if a >= 0 else a + 26


def main():
    s = list(getString())
    t = list(getString())

    u = [diff(s[i], t[i]) for i in range(len(s))]

    print('Yes' if len(set(u)) == 1 else 'No')


if __name__ == "__main__":
    main()
