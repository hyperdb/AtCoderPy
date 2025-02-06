# ABC-390 A - 12435
# https://atcoder.jp/contests/abc390/tasks/abc390_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = [0] + getIntList()

    d = []
    for i in range(1, len(A)):
        if A[i] == i:
            continue
        else:
            d.append(i)

    print("Yes" if len(d) == 2 and d[1] - d[0] == 1 else "No")


if __name__ == "__main__":
    main()
