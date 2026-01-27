# ABC-067 C - Splitting Pile
# https://atcoder.jp/contests/abc067/tasks/arc078_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    sum_left = 0
    sum_right = sum(a)

    diff = -1

    for i in range(N - 1):
        sum_left += a[i]
        sum_right -= a[i]
        diff = abs(sum_left - sum_right) if diff == -1 else min(diff, abs(sum_left - sum_right))

    print(diff)


if __name__ == "__main__":
    main()
