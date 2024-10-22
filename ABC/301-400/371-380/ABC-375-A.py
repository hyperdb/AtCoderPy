# ABC-375 A - Seats
# https://atcoder.jp/contests/abc375/tasks/abc375_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = list(getString())

    c = 0
    for i in range(1, N - 1):
        if S[i] != ".":
            continue
        if S[i - 1] == S[i + 1] == "#":
            c += 1
    print(c)


if __name__ == "__main__":
    main()
