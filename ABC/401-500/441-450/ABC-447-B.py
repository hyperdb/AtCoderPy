# ABC-447 B - mpp
# https://atcoder.jp/contests/abc447/tasks/abc447_b
#
def getString():
    return input()


def main():
    S = getString()

    # それぞれの文字の出現回数を数える
    # collections.Counterでもよい？
    d = dict()
    for c in S:
        d.setdefault(c, 0)
        d[c] += 1

    # 出現回数の最大値を求める
    maxCount = max(d.values())

    # 最大出現回数の文字を除いた文字列を生成する
    t = ""
    for c in S:
        if d[c] == maxCount:
            continue
        t += c

    print(t)


if __name__ == "__main__":
    main()
