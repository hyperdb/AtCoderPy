# ABC-038 B - ディスプレイ
# https://atcoder.jp/contests/abc038/tasks/abc038_b
#
def getIntList():
    return list(map(int, input().split()))


def main():
    HW1 = getIntList()
    HW2 = getIntList()
    side = set(HW1) & set(HW2)

    print("YES" if len(side) > 0 else "NO")


if __name__ == "__main__":
    main()
