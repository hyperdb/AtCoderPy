# ABC-177 B - Substring
# https://atcoder.jp/contests/abc177/tasks/abc177_b
#
def getString():
    return input()


def cnt_diff(s, t):
    c = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            c += 1
    return c


def main():
    s = getString()
    t = getString()

    a = len(s)
    b = len(t)
    c = b
    for i in range(a - b + 1):
        u = s[i:i + b]
        n = cnt_diff(u, t)

        if c > n:
            c = n
    print(c)


if __name__ == "__main__":
    main()
