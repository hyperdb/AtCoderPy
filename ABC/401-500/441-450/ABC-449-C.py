# ABC-449 C - Comfortable Distance
# https://atcoder.jp/contests/abc449/tasks/abc449_c
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    N, L, R = getIntMap()
    S = getString()

    # Rはj - i <= Rの条件を満たすために必要な最小値なので、Rを1増やしておく
    R += 1
    # 文字列を数値に変換してリストAに格納
    # 文字の辞書だとTLEだったので、文字を数値に変換してリストAに格納する方法を採用
    A = [ord(c) - ord("a") for c in S]
    # 文字の出現回数を記録するリストC
    C = [0] * 26

    result = 0
    # 文字の出現位置を記録するために、文字の出現回数を更新しながら条件を満たす組み合わせを数える
    for i in range(N):
        c = A[i]
        # 文字の出現回数を更新して、条件を満たす組み合わせを数える
        # Lより大きい場合は、文字の出現回数を増やす
        if i >= L:
            C[A[i - L]] += 1
        # Rより大きい場合は、文字の出現回数を減らす
        if i >= R:
            C[A[i - R]] -= 1
        result += C[c]

    print(result)


if __name__ == "__main__":
    main()
