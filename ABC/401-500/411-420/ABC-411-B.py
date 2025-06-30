# ABC-411 B - Distance Table
# https://atcoder.jp/contests/abc411/tasks/abc411_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    D = [0] + getIntList()

    for i in range(1, N):
        total = 0
        result = []
        for j in range(i, N):
            total += D[j]
            result.append(total)
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
