# ABC-264 A - "atcoder".substr()
# https://atcoder.jp/contests/abc264/tasks/abc264_a
#
def getIntMap():
    return map(int, input().split())


def main():
    l, r = getIntMap()
    s = "atcoder"

    print(s[l-1:r])


if __name__ == "__main__":
    main()
