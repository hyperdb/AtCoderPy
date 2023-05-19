# ABC-207 A - Repression
# https://atcoder.jp/contests/abc207/tasks/abc207_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()

    l.sort()

    print(l[1] + l[2])


if __name__ == "__main__":
    main()
