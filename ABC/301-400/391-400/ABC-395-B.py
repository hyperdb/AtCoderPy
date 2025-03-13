# ABC-395 B - Make Target
# https://atcoder.jp/contests/abc395/tasks/abc395_b
#
def getInt():
    return int(input())


def main():
    N = getInt()

    A = [["" for _ in range(N)] for _ in range(N)]

    for i in range(1, N + 1):
        j = N + 1 - i
        if i > j:
            continue
        fc = "." if i % 2 == 0 else "#"

        for x in range(i, j + 1):
            for y in range(i, j + 1):
                A[x - 1][y - 1] = fc

    for r in A:
        print("".join(r))


if __name__ == "__main__":
    main()
