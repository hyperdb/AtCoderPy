# ABC-059 C - Sequence
# https://atcoder.jp/contests/abc059/tasks/arc072_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def adjust(A, start):
    total = 0
    count = 0
    for i in range(len(A)):
        total += A[i]
        # プラスから始める場合、偶数番目はプラス、奇数番目はマイナス
        if start:
            if i % 2 == 0:
                if total <= 0:
                    # 0までの回数に1を足す
                    count += abs(total) + 1
                    # 合計は1になる
                    total = 1
            else:
                if total >= 0:
                    count += abs(total) + 1
                    total = -1
        # マイナスから始める場合、偶数番目はマイナス、奇数番目はプラス
        else:
            if i % 2 == 0:
                if total >= 0:
                    count += abs(total) + 1
                    total = -1
            else:
                if total <= 0:
                    count += abs(total) + 1
                    total = 1
    return count


def main():
    _N = getInt()
    A = getIntList()

    c1 = adjust(A, True)
    c2 = adjust(A, False)

    print(min(c1, c2))


if __name__ == "__main__":
    main()
