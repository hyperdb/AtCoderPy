# ABC-191 A - Vanishing Pitch
# https://atcoder.jp/contests/abc191/tasks/abc191_a
#
def getIntMap():
    return map(int, input().split())


def main():
    v, t, s, d = getIntMap()

    a = d / v

    print('No' if t <= a <= s else 'Yes')


if __name__ == "__main__":
    main()
