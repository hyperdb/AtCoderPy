# ABC-076 C - Dubious Document 2
# https://atcoder.jp/contests/abc076/tasks/abc076_c
#
def getString():
    return input()


# sとtがマッチするかどうか（"?"は任意の文字として扱う）
def match_str(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != "?" and s[i] != t[i]:
            return False

    return True


# 文字列の一部分を置き換え
def replace_at(s, i, t):
    return s[:i] + t + s[i + len(t) :]


def main():
    S = getString()
    T = getString()

    match = False
    # 後ろからTを当てはめていく
    for i in range(len(S) - len(T), -1, -1):
        s = S[i : i + len(T)]
        if match_str(s, T):
            match = True
            S = replace_at(S, i, T)
            break

    if not match:
        print("UNRESTORABLE")
    else:
        print(S.replace("?", "a"))


if __name__ == "__main__":
    main()
