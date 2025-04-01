# ABC-396 B - Card Pile
# https://atcoder.jp/contests/abc396/tasks/abc396_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    A = getStringRow(N)

    C = [0 for _ in range(100)]

    for i in range(N):
        if A[i][0] == "2":
            print(C.pop())
        else:
            _, n = map(int, A[i].split(" "))
            C += [n]


if __name__ == "__main__":
    main()
