# ABC-396 A - Triple Four
# https://atcoder.jp/contests/abc396/tasks/abc396_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    B = []
    x = A[0]
    c = 1
    for i in range(1, N):
        if x != A[i]:
            B.append((x, c))
            x = A[i]
            c = 1
        else:
            c += 1

    B.append((x, c))

    r = False
    for _, c in B:
        if c >= 3:
            r = True
            break

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
