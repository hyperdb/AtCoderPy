# ABC-122 B - ATCoder
# https://atcoder.jp/contests/abc122/tasks/abc122_b
#
import re


def getString():
    return input()


def main():
    s = getString()

    pattern = r'^([ACGT]{1,}).*'

    l = 0
    for i in range(len(s)):
        m = re.search(pattern, s[i:])
        if m:
            x = len(m.group(1))
            l = x if x > l else l
    print(l)


if __name__ == "__main__":
    main()
