# ABC-222 B - Failing Grade
# https://atcoder.jp/contests/abc222/tasks/abc222_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, p = getIntMap()
    a = getIntList()
    b = [i for i in a if i < p]

    print(len(b))


if __name__ == "__main__":
    main()
