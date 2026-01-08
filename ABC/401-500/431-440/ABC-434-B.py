# ABC-434 B - Bird Watching
# https://atcoder.jp/contests/abc434/tasks/abc434_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    AB = getIntListRow(N)

    counter = [[0, 0] for _ in range(M + 1)]
    for a, b in AB:
        counter[a][0] += 1  # count
        counter[a][1] += b  # sum

    for sa, sb in counter[1:]:
        print(sb / sa)


if __name__ == "__main__":
    main()
