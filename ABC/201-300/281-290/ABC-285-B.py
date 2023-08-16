# ABC-285 B - Longest Uncommon Prefix
# https://atcoder.jp/contests/abc285/tasks/abc285_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = list(getString())

    for i in range(1, len(s)):
        l = 0
        for j in range(len(s) - i):
            if s[j] == s[j + i]:
                break
            l += 1
        print(l)


if __name__ == "__main__":
    main()
