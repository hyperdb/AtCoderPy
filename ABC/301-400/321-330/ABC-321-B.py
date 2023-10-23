# ABC-321 B - Cutoff
# https://atcoder.jp/contests/abc321/tasks/abc321_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    a = getIntList()

    high = max(a)
    low = min(a)
    goal = x - (sum(a) - high - low)

    if goal > high:
        print(-1)
    elif low < goal <= high:
        print(goal)
    elif goal <= low:
        print(0)


if __name__ == "__main__":
    main()
