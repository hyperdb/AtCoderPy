# ABC-320 B - Longest Palindrome
# https://atcoder.jp/contests/abc320/tasks/abc320_b
#
def getString():
    return input()


def main():
    s = getString()

    c = 0
    for i in range(len(s), 0, -1):
        for j in range(0, len(s) - i + 1):
            w = s[j:j+i]
            r = w[::-1]
            if w == r:
                c = i
                break
        if c > 0:
            break
    print(c)


if __name__ == "__main__":
    main()
