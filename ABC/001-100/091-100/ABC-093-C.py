# ABC-093 C - Same Integers
# https://atcoder.jp/contests/abc093/tasks/arc094_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    ABC = getIntList()
    # 偶数と奇数の数を数える
    odd = 0
    even = 0
    for i in ABC:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    result = 0
    # 全体の偶数・奇数を合わせる
    # 偶数が2つある場合は、偶数を1増やす
    if even == 2:
        ABC = [i + 1 if i % 2 == 0 else i for i in ABC]
        result += 1
    # 奇数が2つある場合は、奇数を1増やす
    elif odd == 2:
        ABC = [i + 1 if i % 2 == 1 else i for i in ABC]
        result += 1

    # 最大値との差を求める
    diff = [max(ABC) - i for i in ABC]
    # 差の合計を2で割る（1回で2増やす操作）
    result += sum(diff) // 2

    print(result)


if __name__ == "__main__":
    main()
