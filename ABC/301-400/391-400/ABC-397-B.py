# ABC-397 B - Ticket Gate Log
# https://atcoder.jp/contests/abc397/tasks/abc397_b
#
def getString():
    return input()


def main():
    S = getString()

    ss = len(S)

    if S[0] != "i":
        S = "i" + S
    if S[-1] != "o":
        S += "o"

    while True:
        if S.find("ii") < 0:
            break
        S = S.replace("ii", "ioi")

    while True:
        if S.find("oo") < 0:
            break
        S = S.replace("oo", "oio")

    print(len(S) - ss)


if __name__ == "__main__":
    main()
