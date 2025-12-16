# ABC-427 B - Sum of Digits Sequence
# https://atcoder.jp/contests/abc427/tasks/abc427_b
#
def getInt():
    return int(input())


def colSum(N):
    return N if N < 10 else sum([int(i) for i in list(str(N))])


def main():
    N = getInt()
    A = [0] * (N + 1)

    A[0] = 1
    for i in range(1, N + 1):
        for j in range(i):
            A[i] += colSum(A[j])
    print(A[-1])


if __name__ == "__main__":
    main()
