# ABC-075 A - One out of Three
# https://atcoder.jp/contests/abc075/tasks/abc075_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()
    l.sort()

    print(l[0] if l[0] != l[1] else l[2])


if __name__ == "__main__":
    main()
