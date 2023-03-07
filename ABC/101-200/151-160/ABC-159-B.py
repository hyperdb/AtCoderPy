# ABC-159 B - String Palindrome
# https://atcoder.jp/contests/abc159/tasks/abc159_b
#
def getString():
    return input()


def palindrome(s):
    r = s[::-1]

    return True if s == r else False


def main():
    s = getString()

    l = len(s)
    t = s[:(l - 1) // 2]
    u = s[(l + 3) // 2 - 1:]

    print('Yes' if palindrome(s) and palindrome(t) and palindrome(u) else 'No')


if __name__ == "__main__":
    main()
