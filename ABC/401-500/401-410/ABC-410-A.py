# ABC-410 A - G1
# https://atcoder.jp/contests/abc410/tasks/abc410_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()
    K = getInt()

    count = 0
    for i in A:
        if i >= K:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
