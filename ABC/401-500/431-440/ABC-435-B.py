# ABC-435 B - No-Divisible Range
# https://atcoder.jp/contests/abc435/tasks/abc435_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()

    c = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            s = sum(A[i : j + 1])
            c += 1  # count up
            for k in range(i, j + 1):
                _, m = divmod(s, A[k])
                # if divisible, roll back count
                if m == 0:
                    c -= 1
                    break
    print(c)


if __name__ == "__main__":
    main()
