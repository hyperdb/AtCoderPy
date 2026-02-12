# ABC042 B - 文字列大好きいろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_b
#
def getIntMap() -> tuple[int, ...]:
    return tuple(map(int, input().split()))


def getStringRow(N: int) -> list[str]:
    return [input() for _ in range(N)]


def main():
    N: int
    N, _ = getIntMap()  # Lは使わない
    S: list[str] = sorted(getStringRow(N))
    # S.sort()
    print("".join(S))


if __name__ == "__main__":
    main()
