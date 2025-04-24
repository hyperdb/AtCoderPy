# ABC-401 B - Unauthorized
# https://atcoder.jp/contests/abc401/tasks/abc401_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    stat = 0
    error = 0
    for a in S:
        if a == "login":
            stat = 1
        elif a == "logout":
            stat = 0
        elif a == "public":
            pass
        elif a == "private":
            if stat == 0:
                error += 1
    print(error)


if __name__ == "__main__":
    main()
