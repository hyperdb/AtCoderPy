# ABC-457 A - Array
# https://atcoder.jp/contests/abc457/tasks/abc457_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()
    X = getInt()

    print(A[X])


if __name__ == "__main__":
    main()
