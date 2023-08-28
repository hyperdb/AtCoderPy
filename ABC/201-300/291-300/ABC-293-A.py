# ABC-293 A - Swap Odd and Even
# https://atcoder.jp/contests/abc293/tasks/abc293_a
#
def getString():
    return input()


def main():
    s = getString()
    t = ''

    i = 0
    while i < len(s):
        t += (s[i:i+2])[::-1]
        i += 2
    print(t)


if __name__ == "__main__":
    main()
