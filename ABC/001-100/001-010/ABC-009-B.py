# B - 心配性な富豪、ファミリーレストランに行く。
# https://atcoder.jp/contests/abc009/tasks/abc009_2
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    N = getInt()
    A = getIntRow(N)

    A = list(set(A))
    A.sort()

    print(A[-2])


if __name__ == "__main__":
    main()
