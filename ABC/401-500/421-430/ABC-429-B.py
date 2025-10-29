# ABC-429 B - N - 1
# https://atcoder.jp/contests/abc429/tasks/abc429_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = getIntList()

    sa = sum(A)
    r = False
    for i in range(N):
        if sa - A[i] == M:
            r = True
            break
    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
