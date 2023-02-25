# ABC-147 B - Palindrome-philia
# https://atcoder.jp/contests/abc147/tasks/abc147_b
#
def getString():
    return input()


def main():
    s = getString()

    l = len(s) // 2
    a = list(s[0:l])
    b = list(s[-1 * l:])
    b.reverse()

    c = 0
    for i in range(l):
        if a[i] != b[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
