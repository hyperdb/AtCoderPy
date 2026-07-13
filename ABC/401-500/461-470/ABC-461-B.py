# ABC-461 B - The Honest Woodcutters
# https://atcoder.jp/contests/abc461/tasks/abc461_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()
    B = [0] + getIntList()

    result = True
    for i in range(1, N + 1):
        # 木こりの申告通りなら続ける
        if B[A[i]] == i:
            continue
        # そうでなければ、結果はNo
        result = False
        break
    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
