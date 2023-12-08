# ABC-329 B - Next
# https://atcoder.jp/contests/abc329/tasks/abc329_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    b = [x for x in a if x < max(a)]
    print(max(b))


if __name__ == "__main__":
    main()
