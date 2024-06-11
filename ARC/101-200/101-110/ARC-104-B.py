# ARC-104 B - DNA Sequence
# https://atcoder.jp/contests/arc104/tasks/arc104_b
#
def getStringMap():
    return input().split()


def main():
    N, S = getStringMap()

    r = 0
    for i in range(int(N)):
        at = 0
        cg = 0
        for c in S[i:]:
            if c == 'A':
                at += 1
            if c == 'T':
                at -= 1
            if c == 'C':
                cg += 1
            if c == 'G':
                cg -= 1
            if at == 0 and cg == 0:
                r += 1
    print(r)


if __name__ == "__main__":
    main()
