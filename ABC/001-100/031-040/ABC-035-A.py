# ABC-035 A - テレビ
# https://atcoder.jp/contests/abc035/tasks/abc035_a
#
def getIntMap():
    return map(int, input().split())


def main():
    W, H = getIntMap()

    print('16:9' if W % 16 == 0 and H % 9 == 0 else '4:3')


if __name__ == "__main__":
    main()
