# ABC-392 B - Who is Missing?
# https://atcoder.jp/contests/abc392/tasks/abc392_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = [0] + getIntList()
    A.sort()

    B = []
    for i in range(1, M + 1):
        d = A[i] - A[i - 1]
        if d > 1:
            B += [x for x in range(A[i - 1] + 1, A[i])]

    B += [x for x in range(A[i] + 1, N + 1)]

    print(len(B))
    print(" ".join(map(str, B)) if len(B) > 0 else "")


if __name__ == "__main__":
    main()
