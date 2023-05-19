# ABC-228 A - On and Off
# https://atcoder.jp/contests/abc228/tasks/abc228_a
#
def getIntMap():
    return map(int, input().split())


def main():
    s, t, x = getIntMap()

    if s < t:
        print('Yes' if s <= x < t else 'No')
    else:
        print('No' if t <= x < s else 'Yes')


if __name__ == "__main__":
    main()
