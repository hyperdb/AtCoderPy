# ABC-358 B - Ticket Counter
# https://atcoder.jp/contests/abc358/tasks/abc358_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, A = getIntMap()
    T = getIntList()

    r = []

    p = T[0] + A
    r.append(p)
    for i in range(1, N):
        if p < T[i]:
            p += (T[i] - p)
        p += A
        r.append(p)

    print("\n".join(map(str, r)))


if __name__ == "__main__":
    main()
