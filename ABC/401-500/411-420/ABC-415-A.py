# ABC-415 A - Unsupported Type
# https://atcoder.jp/contests/abc415/tasks/abc415_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()
    X = getInt()

    print("Yes" if X in A else "No")


if __name__ == "__main__":
    main()
