# ABC-393 B - A..B..C
# https://atcoder.jp/contests/abc393/tasks/abc393_b
#
def getString():
    return input()


def main():
    S = list(getString())

    c = 0
    for x in [i for i in range(len(S)) if S[i] == "A"]:
        for y in [i for i in range(x + 1, len(S)) if S[i] == "B"]:
            for z in [i for i in range(y + 1, len(S)) if S[i] == "C"]:
                if x + z == 2 * y:  # 等差中項
                    c += 1
    print(c)


if __name__ == "__main__":
    main()
