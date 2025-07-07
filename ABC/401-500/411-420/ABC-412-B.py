# ABC-412 B - Precondition
# https://atcoder.jp/contests/abc412/tasks/abc412_b
#
def getString():
    return input()


def main():
    S = getString()
    T = getString()

    ret = True
    for i in range(1, len(S)):
        if S[i] < "a":
            if S[i - 1] in T:
                continue
            else:
                ret = False
                break

    print("Yes" if ret else "No")


if __name__ == "__main__":
    main()
