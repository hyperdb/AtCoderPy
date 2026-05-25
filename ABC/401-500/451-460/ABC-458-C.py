# ABC-458 C - C Stands for Center
# https://atcoder.jp/contests/abc458/tasks/abc458_c
#
def getString():
    return input()


def main():
    S = getString()

    result = 0
    for i in range(len(S)):
        # 中央の"C"を探す
        if S[i] != "C":
            continue
        # 前後の文字数を数える
        before = i
        after = len(S) - i - 1
        # 小さい方の文字数に"C"だけの1を足す
        result += min(before, after) + 1

    print(result)


if __name__ == "__main__":
    main()
