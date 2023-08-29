# ABC-294 A - Filter
# https://atcoder.jp/contests/abc294/tasks/abc294_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = [i for i in a if i % 2 == 0]

    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
