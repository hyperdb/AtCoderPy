# ABC-425 B - Find Permutation 2
# https://atcoder.jp/contests/abc425/tasks/abc425_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()

    B = [a for a in A if a > 0]

    result = True
    for b in B:
        if B.count(b) > 1 or b > N:
            result = False
            break
    if not result:
        print("No")
    else:
        C = [i for i in range(1, N + 1) if i not in B]

        j = 0
        for i in range(1, N + 1):
            if A[i] in B:
                continue
            else:
                A[i] = C[j]
                j += 1
        print("Yes")
        print(" ".join(map(str, A[1:])))


if __name__ == "__main__":
    main()
