# ABC-046 A - AtCoDeerくんとペンキ
# https://atcoder.jp/contests/abc046/tasks/abc046_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()
    print(len(list(set(l))))


if __name__ == "__main__":
    main()
