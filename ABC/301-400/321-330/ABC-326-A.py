# ABC-326 A - 2UP3DOWN
# https://atcoder.jp/contests/abc326/tasks/abc326_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    d = y - x
    print('No' if d > 2 or d < -3 else 'Yes')


if __name__ == "__main__":
    main()
