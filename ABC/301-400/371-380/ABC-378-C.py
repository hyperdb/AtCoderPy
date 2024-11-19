# ABC-378 C - Repeating
# https://atcoder.jp/contests/abc378/tasks/abc378_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()
    d = dict()

    for x in set(A):
        d[x] = -1

    B = []
    for i in range(1, len(A)):
        B.append(d[A[i]])
        d[A[i]] = i

    print(" ".join(map(str, B)))


if __name__ == "__main__":
    main()
