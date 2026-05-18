# ABC-454 B - Mapping
# https://atcoder.jp/contests/abc454/tasks/abc454_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    F = getIntList()

    print("Yes" if len(set(F)) == len(F) else "No")
    print("Yes" if len(set(F)) == M else "No")


if __name__ == "__main__":
    main()
