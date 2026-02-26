# ABC-089 C - March
# https://atcoder.jp/contests/abc089/tasks/abc089_c
#
import itertools


def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    # 条件の頭文字でカウントする
    T = dict.fromkeys(["M", "A", "R", "C", "H"], 0)
    for s in S:
        if s[0] in T:
            T[s[0]] += 1

    # 使用された文字だけを組み合わせる
    C = [key for key, value in T.items() if value > 0]
    c = itertools.combinations(C, 3)

    result = 0
    for d in c:
        # 組み合わせの文字のそれぞれの個数を掛け合わせる
        result += T[d[0]] * T[d[1]] * T[d[2]]

    print(result)


if __name__ == "__main__":
    main()
