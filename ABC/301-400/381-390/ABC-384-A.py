# ABC-384 A - aaaadaa
# https://atcoder.jp/contests/abc384/tasks/abc384_a
#
def getStringMap():
    return input().split()


def getString():
    return input()


def main():
    N, c1, c2 = getStringMap()
    S = getString()

    buf = []
    for c in S:
        buf.append(c1 if c == c1 else c2)
    print("".join(buf))


if __name__ == "__main__":
    main()
