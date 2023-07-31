# ABC-275 A - Find Takahashi
# https://atcoder.jp/contests/abc275/tasks/abc275_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    h = getIntList()

    print(h.index(max(h)) + 1)


if __name__ == "__main__":
    main()
