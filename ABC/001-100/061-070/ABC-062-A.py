# ABC-062 A - Grouping
# https://atcoder.jp/contests/abc062/tasks/abc062_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    s = [4, 6, 9, 11]

    print('No' if a == 2 or b == 2 else 'No' if (a in s) ^ (b in s) else 'Yes')


if __name__ == "__main__":
    main()
