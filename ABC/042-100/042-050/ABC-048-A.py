# ABC-048 A - AtCoder *** Contest
# https://atcoder.jp/contests/abc048/tasks/abc048_a
#
def getStringList():
    return input().split()


def main():
    d = getStringList()

    v = ''
    for s in d:
        v += s[0]
    print(v)


if __name__ == "__main__":
    main()
