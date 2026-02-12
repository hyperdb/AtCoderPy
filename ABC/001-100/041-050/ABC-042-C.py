# 042 C - こだわり者いろはちゃん
# https://atcoder.jp/contests/abc042/tasks/arc058_a
#
def getIntList() -> list[int]:
    return list(map(int, input().split()))


def getIntMap() -> tuple[int, ...]:
    return tuple(map(int, input().split()))


def check_num(n: int, error_data: list[int]) -> bool:
    for digit in set(list(map(int, list(str(n))))):
        if digit in error_data:
            return False
    return True


def main():
    N: int
    N, _ = getIntMap()  # Kは使わない
    D: list[int] = getIntList()

    for c in range(N, 100000):
        if check_num(c, D):
            print(c)
            break


if __name__ == "__main__":
    main()
