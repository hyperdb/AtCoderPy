# ABC-445 C - Sugoroku Destination
# https://atcoder.jp/contests/abc445/tasks/abc445_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()
    # 最終的な行き先を保存するための配列
    B = [0] * (N + 1)
    # 解答を保存するための配列
    ans = [0] * (N + 1)

    # Aを順番に見ていく
    for n in range(1, N + 1):
        p = A[n]
        # 経路を保存
        t = [p]
        # 10**100回繰り返す
        for _ in range(10**100):
            # 同じ場所に戻ったら、そこから先は同じ経路になるので、保存している場所を追加する
            if p == A[p]:
                break

            p = A[p]
            b = B[p]
            # 保存済みの場所に行ったら、そこから先は同じ経路になるので、保存している場所を追加する
            if b != 0:
                t.append(b)
                break

            # 経路を保存
            t.append(p)

        # 解答用に経路の最後の場所を保存する
        ans[n] = t[-1]

        # 経路ごとに最後の場所を保存する
        for i in range(len(t)):
            p = t[i]
            if B[p] == 0:
                B[p] = t[-1]

    print(" ".join(map(str, ans[1:])))


if __name__ == "__main__":
    main()
