# ABC-043 C - いっしょ
# https://atcoder.jp/contests/abc043/tasks/arc059_a
#
import math


def getInt() -> int:
    return int(input())


def getIntList() -> list[int]:
    return list(map(int, input().split()))


def getCost(data: list[int], n: int) -> int:
    c = 0
    for d in data:
        c += pow(d - n, 2)
    return c


def main():
    N: int = getInt()

    if N > 0:
        data: list[int] = getIntList()
        ave: float = sum(data) / len(data)
        cost: int = 0
        if ave.is_integer():
            cost = getCost(data, int(ave))
        else:
            cost = min(getCost(data, math.floor(ave)), getCost(data, math.ceil(ave)))
        print(cost)

    else:
        print(0)


if __name__ == "__main__":
    main()
