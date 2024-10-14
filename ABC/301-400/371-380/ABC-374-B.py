# ABC-374 B - Unvarnished Report
# https://atcoder.jp/contests/abc374/tasks/abc374_b
#
def getString():
    return input()


def main():
    S = getString()
    T = getString()

    if S == T:
        print(0)
    else:
        ls = len(S)
        lt = len(T)

        r = False
        c = min(ls, lt)
        for i in range(c):
            if S[i] == T[i]:
                continue
            else:
                print(i + 1)
                r = True
                break

        if not r:
            print(c + 1)


if __name__ == "__main__":
    main()
