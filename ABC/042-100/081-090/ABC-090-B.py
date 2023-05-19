# ABC-090 B - Palindromic Numbers
# https://atcoder.jp/contests/abc090/tasks/abc090_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    r = 0
    for i in range(a, b + 1):
        s = str(i)
        if s[0] == s[4] and s[1] == s[3]:
            r += 1
    print(r)


if __name__ == "__main__":
    main()
