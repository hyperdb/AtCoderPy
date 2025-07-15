# ABC-413 A - Content Too Large
# https://atcoder.jp/contests/abc413/tasks/abc413_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = getIntList()

    print("Yes" if sum(A) <= M else "No")


if __name__ == "__main__":
    main()
