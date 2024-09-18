# ABC-370 C - Word Ladder
# https://atcoder.jp/contests/abc370/tasks/abc370_c
#
def getString():
    return input()


def replaceChar(s, i, c):
    return s[:i] + [c] + s[i + 1 :]


def main():
    S = list(getString())
    T = list(getString())

    X = []
    while S != T:
        n = []
        for i in range(len(S)):
            if S[i] != T[i]:
                n.append(i)

        a = []
        for j in n:
            a.append("".join(replaceChar(S, j, T[j])))

        a.sort()
        X.append(a[0])

        S = list(a[0])

    print(len(X))
    for s in X:
        print(s)


if __name__ == "__main__":
    main()
