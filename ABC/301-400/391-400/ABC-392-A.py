# ABC-392 A - Shuffled Equation
# https://atcoder.jp/contests/abc392/tasks/abc392_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = getIntList()
    A.sort()

    print("Yes" if A[0] * A[1] == A[2] else "No")


if __name__ == "__main__":
    main()
