# ABC-432 B - Permute to Minimize
# https://atcoder.jp/contests/abc432/tasks/abc432_b
#
def getString():
    return input()


def main():
    N = [int(s) for s in list(getString())]

    N.sort()

    if (N.index(0) if 0 in N else -1) == -1:
        print(int("".join(map(str, N))))
    else:
        M = [n for n in N if n > 0]
        print(str(M[0]) + "0" * N.count(0) + "".join(map(str, M[1:])))


if __name__ == "__main__":
    main()
