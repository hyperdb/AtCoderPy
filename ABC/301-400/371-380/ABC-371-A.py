# ABC-371 A - Jiro
# https://atcoder.jp/contests/abc371/tasks/abc371_a
#
def getStringMap():
    return input().split()


def main():
    S = getStringMap()
    a = b = c = 0

    if S[0] == ">":
        a += 1
    else:
        b += 1

    if S[1] == ">":
        a += 1
    else:
        c += 1

    if S[2] == ">":
        b += 1
    else:
        c += 1

    print("A" if a == 1 else "B" if b == 1 else "C")


if __name__ == "__main__":
    main()
