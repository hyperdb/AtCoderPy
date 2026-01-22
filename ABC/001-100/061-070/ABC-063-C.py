# ABC-063 C - Bugged
# https://atcoder.jp/contests/abc063/tasks/arc075_a
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    N = getInt()
    s = getIntRow(N)

    A = [a for a in s if a % 10 == 0]
    B = [b for b in s if b % 10 != 0]

    # 端数がなければ0を出力して終了
    if len(B) == 0:
        print(0)
        return

    sumA = sum(A)
    sumB = sum(B)

    # 端数の合計が10の倍数なら最小値を引く
    if sumB % 10 == 0:
        sumB -= min(B)

    print(sumA + sumB)


if __name__ == "__main__":
    main()
