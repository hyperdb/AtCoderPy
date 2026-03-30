# ABC-450 B - Split Ticketing
# https://atcoder.jp/contests/abc450/tasks/abc450_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    C = []

    # 料金表を取得（位置合わせで0を追加）
    for i in range(N - 1):
        c = [0] * (i + 1) + getIntList()
        C.append(c)

    # 3点を選んで条件を満たせばYes、満たさなければNo
    for x in range(N - 2):
        for y in range(x + 1, N - 1):
            for z in range(y + 1, N):
                if C[x][z] > C[x][y] + C[y][z]:
                    print("Yes")
                    return

    print("No")


if __name__ == "__main__":
    main()
