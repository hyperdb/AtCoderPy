# ABC-073 C - Write and Erase
# https://atcoder.jp/contests/abc073/tasks/abc073_c
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    N = getInt()
    A = getIntRow(N)
    B = set()

    for a in A:
        if a in B:
            B.remove(a)
        else:
            B.add(a)

    print(len(B))


if __name__ == "__main__":
    main()
