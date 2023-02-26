# ABC-148 B - Strings with the Same Length
# https://atcoder.jp/contests/abc148/tasks/abc148_b
#
def getInt():
    return int(input())


def getStringMap():
    return input().split()


def main():
    n = getInt()
    s, t = getStringMap()

    a = ''
    for i in range(n):
        a += (s[i] + t[i])
    print(a)


if __name__ == "__main__":
    main()
