# ABC042 A - 和風いろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_a
#
def getIntList() -> list[int]:
    return list(map(int, input().split()))


def main():
    d: list[int] = sorted(getIntList())
    # d.sort()
    print("YES" if d == [5, 5, 7] else "NO")


if __name__ == "__main__":
    main()
