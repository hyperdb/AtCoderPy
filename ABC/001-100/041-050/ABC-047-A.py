# ABC-047 A - キャンディーと2人の子供
# https://atcoder.jp/contests/abc047/tasks/abc047_a
#
def getIntList() -> list[int]:
    return list(map(int, input().split()))


def main():
    D: list[int] = getIntList()
    D.sort()

    print("Yes" if D[2] == D[0] + D[1] else "No")


if __name__ == "__main__":
    main()
