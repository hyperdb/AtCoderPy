# ABC-371 B - Taro
# https://atcoder.jp/contests/abc371/tasks/abc371_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    N, M = getIntMap()
    AB = getStringListRow(M)

    c = [0] + [0 for _ in range(N)]

    for A, B in AB:
        if B == "F":
            print("No")
            continue
        print("Yes" if c[int(A)] == 0 else "No")
        c[int(A)] += 1


if __name__ == "__main__":
    main()
