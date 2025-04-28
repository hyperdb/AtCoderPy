# ABC-402 B - Restaurant Queue
# https://atcoder.jp/contests/abc402/tasks/abc402_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    Q = getInt()
    query = getIntListRow(Q)

    m = []
    c = 0
    for s in query:
        if s[0] == 1:
            m.append(s[1])
        else:
            c += 1

    for i in range(c):
        print(m[i])


if __name__ == "__main__":
    main()
