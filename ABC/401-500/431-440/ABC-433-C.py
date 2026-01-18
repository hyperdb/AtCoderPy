# ABC-433 C - 1122 Substring 2
# https://atcoder.jp/contests/abc433/tasks/abc433_c
#
def getString():
    return input()


def main():
    S = getString()

    prev_c = ""
    cnt = 0
    a = []
    for c in S:
        if c != prev_c:
            a.append((prev_c, cnt))
            prev_c = c
            cnt = 1
        else:
            cnt += 1
    a.append((prev_c, cnt))

    r = 0
    for i in range(1, len(a) - 1):
        v1, c1 = a[i]
        v2, c2 = a[i + 1]
        if int(v1) + 1 == int(v2):
            r += min(c1, c2)
    print(r)


if __name__ == "__main__":
    main()
