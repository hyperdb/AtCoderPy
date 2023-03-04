# ABC-155 A - Poor
# https://atcoder.jp/contests/abc155/tasks/abc155_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()

    print('Yes' if len(set(l)) == 2 else 'No')


if __name__ == "__main__":
    main()
