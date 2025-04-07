# ABC-399 A - Hamming Distance
# https://atcoder.jp/contests/abc399/tasks/abc399_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()
    T = getString()

    c = 0
    for i in range(N):
        if S[i] != T[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
