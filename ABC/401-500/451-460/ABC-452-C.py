# ABC-452 C - Fishbones
# https://atcoder.jp/contests/abc452/tasks/abc452_c
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    AB = getIntListRow(N)
    M = getInt()
    S = getStringRow(M)

    # i文字目に出現する文字セットをT[i]に格納する
    T = [set() for _ in range(N)]
    for s in S:
        # b文字目に出現する文字をT[i]に追加する
        for i in range(N):
            a, b = AB[i]
            # 文字列sの長さがa以外は対象外
            if len(s) == a:
                T[i].add(s[b - 1])

    # Sの各文字列について、i文字目がT[i]に含まれているかを確認する
    for i in range(M):
        result = True
        # 文字列S[i]の長さがNと異なる場合は対象外
        if len(S[i]) != N:
            result = False
        else:
            for j in range(len(S[i])):
                # 文字列S[i]のj文字目がT[j]に含まれていない場合は対象外
                if S[i][j] not in T[j]:
                    result = False
                    break

        print("Yes" if result else "No")


if __name__ == "__main__":
    main()
