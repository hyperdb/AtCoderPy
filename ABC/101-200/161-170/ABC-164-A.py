# ABC-164 A - Sheep and Wolves
# https://atcoder.jp/contests/abc164/tasks/abc164_a
#
def getIntMap():
    return map(int, input().split())


def main():
    s, w = getIntMap()

    print('unsafe' if s <= w else 'safe')


if __name__ == "__main__":
    main()
