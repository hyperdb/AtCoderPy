# ABC-447 C - Insert and Erase A
# https://atcoder.jp/contests/abc447/tasks/abc447_c
#
def getString():
    return input()


def removeA(s):
    ret = []
    for i in range(len(s)):
        if s[i] != "A":
            ret.append(s[i])
    return ret


def countA(s):
    count = 0
    ret = []
    for i in range(len(s)):
        if s[i] == "A":
            count += 1
            continue
        else:
            ret.append(count)
            count = 0

    ret.append(count)

    return ret


def main():
    S = list(getString())
    T = list(getString())

    # S と T が同じならば操作は不要
    if S == T:
        print(0)
    else:
        # "A"を除いた文字列を生成
        sx = removeA(S)
        tx = removeA(T)
        # "A"以外の文字で分割して、"A"の数を数える
        sa = countA(S)
        ta = countA(T)

        # "A"以外の文字が同じでなければ、操作は不可能
        if sx != tx:
            print(-1)
        else:
            # "A"以外の文字で分割されている"A"の数を揃える
            count = 0
            for i in range(len(sa)):
                if sa[i] != ta[i]:
                    count += abs(sa[i] - ta[i])

            print(count)


if __name__ == "__main__":
    main()
