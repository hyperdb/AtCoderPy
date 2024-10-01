# ABC-372 B - 3^A
# https://atcoder.jp/contests/abc372/tasks/abc372_b
#
def getInt():
    return int(input())


def main():
    M = getInt()
    C = []
    A = []

    while M > 0:
        M, m = divmod(M, 3)
        C.append(m)

    for i in range(len(C)):
        j = C[i]
        if j > 0:
            for _ in range(j):
                A.append(i)

    print(len(A))
    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
