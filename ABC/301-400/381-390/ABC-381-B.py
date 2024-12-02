# ABC-391 B - 1122 String
# https://atcoder.jp/contests/abc381/tasks/abc381_b
#
def getString():
    return input()


def main():
    S = list(getString())

    r = False
    if len(S) % 2 == 0 and len(set(S)) == len(S) // 2:
        a = [S[i] for i in range(0, len(S), 2)]
        b = [S[i] for i in range(1, len(S), 2)]

        if a == b:
            r = True

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
