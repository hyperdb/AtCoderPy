#
#
#
import collections


def getStringMap():
    return input().split()


def main():
    N, S = getStringMap()

    w = len(S)
    for i in range(w - 1):
        for j in range(i + 2, w + 1, 2):
            c = collections.Counter(S[i:j])
            if len(c.keys()) % 2 != 0:
                continue


if __name__ == "__main__":
    main()
