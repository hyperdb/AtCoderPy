# ABC-419 A - Too Many Requests
# https://atcoder.jp/contests/abc429/tasks/abc429_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    for _ in range(M if M <= N else N):
        print("OK")
    for _ in range(N - M):
        print("Too Many Requests")


if __name__ == "__main__":
    main()
