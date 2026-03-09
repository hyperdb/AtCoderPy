# ABC-447 A - Seats 2
# https://atcoder.jp/contests/abc447/tasks/abc447_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    # 2席を1組にして数える（余った席はそのまま追加）
    print("Yes" if (N // 2 + N % 2) >= M else "No")


if __name__ == "__main__":
    main()
