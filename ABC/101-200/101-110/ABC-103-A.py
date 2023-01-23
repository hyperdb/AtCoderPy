# ABC-103 A - Task Scheduling Problem
# https://atcoder.jp/contests/abc103/tasks/abc103_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    a = getIntList()

    a.sort()

    print(a[2] - a[0])


if __name__ == "__main__":
    main()
