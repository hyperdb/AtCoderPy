# ABC-192 B - uNrEaDaBlE sTrInG
# https://atcoder.jp/contests/abc192/tasks/abc192_b
#
def getString():
    return input()


def main():
    s = getString()

    s0 = "".join([s[i] for i in range(len(s)) if (i + 1) % 2 == 0])
    s1 = "".join([s[i] for i in range(len(s)) if (i + 1) % 2 != 0])

    print('Yes' if s0 == s0.upper() and s1 == s1.lower() else 'No')


if __name__ == "__main__":
    main()
