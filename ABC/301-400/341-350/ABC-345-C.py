# ABC-345 C - One Time Swap
# https://atcoder.jp/contests/abc345/tasks/abc345_c
#
def getString():
    return input()


def main():
    s = getString()

    # 使われている文字を収集
    d = dict()
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1

    # 使用数が2以上の文字があれば基準を1に（元の文字列）
    r = 1 if len([key for key, value in d.items() if value >= 2]) > 0 else 0

    # 使われている文字を数える
    k = list(d.keys())
    l = len(k)

    # 2種以上あれば組み合わせで計算
    if l >= 2:
        for i in range(l):
            for j in range(i + 1, l):
                r += (d[k[i]] * d[k[j]])

    print(r)


if __name__ == "__main__":
    main()
