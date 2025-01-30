# ABC-388 C - Various Kagamimochi
# https://atcoder.jp/contests/abc388/tasks/abc388_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    mx = max(A)
    c = 1
    r = 0
    for i in range(N - 1):
        a = A[i]
        b = a * 2
        if b > mx:
            break

        for j in range(c, N):
            if A[j] < b:
                continue
            else:
                c = j
                r += N - j
                break
    print(r)


if __name__ == "__main__":
    main()
