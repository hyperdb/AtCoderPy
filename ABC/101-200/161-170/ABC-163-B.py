# ABC-163 B - Homework
# https://atcoder.jp/contests/abc163/tasks/abc163_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    a = getIntList()

    b = n - sum(a)

    print(b if b >= 0 else -1)


if __name__ == "__main__":
    main()
