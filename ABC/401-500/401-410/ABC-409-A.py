# ABC-409 A - Conflict
# https://atcoder.jp/contests/abc409/tasks/abc409_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    T = getString()
    A = getString()

    result = False
    for i in range(N):
        if T[i] == A[i] == "o":
            result = True
            break

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
