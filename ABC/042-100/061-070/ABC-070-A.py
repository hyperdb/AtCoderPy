# ABC-070 A - Palindromic Number
# https://atcoder.jp/contests/abc070/tasks/abc070_a
#
def getString():
    return input()


def main():
    s = getString()
    r = s[::-1]

    print('Yes' if s == r else 'No')


if __name__ == "__main__":
    main()
