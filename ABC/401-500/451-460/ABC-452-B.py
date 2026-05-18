# ABC-452 B - Draw Frame
# https://atcoder.jp/contests/abc452/tasks/abc452_b
#
def getIntMap():
    return map(int, input().split())


def main():
    H, W = getIntMap()

    print("#" * W)
    for _ in range(H - 2):
        print("#" + "." * (W - 2) + "#")
    print("#" * W)


if __name__ == "__main__":
    main()
