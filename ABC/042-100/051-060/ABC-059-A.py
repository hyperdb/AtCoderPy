# ABC-059 A - Three-letter acronym
# https://atcoder.jp/contests/abc059/tasks/abc059_a
#
def getStringList():
    return list(input().split())


def main():
    s = getStringList()

    r = ''
    for w in s:
        r += w[0]
    print(r.upper())


if __name__ == "__main__":
    main()
