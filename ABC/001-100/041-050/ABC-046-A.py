# ABC-046 A - AtCoDeerくんとペンキ
# https://atcoder.jp/contests/abc046/tasks/abc046_a
#
def getIntList() -> list[int]:
    return list(map(int, input().split()))


def main():
    L = getIntList()
    print(len(list(set(L))))


if __name__ == "__main__":
    main()
