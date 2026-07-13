# ABC-464 B - Crop
# https://atcoder.jp/contests/abc464/tasks/abc464_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    H, W = getIntMap()
    S = getStringRow(H)

    # 上部の白行を削除
    delete_row = -1
    for i in range(len(S)):
        if S[i].count("#") == 0:
            delete_row = i
            continue
        break
    if delete_row != -1:
        S = S[delete_row + 1 :]

    # 下部の白行を削除
    delete_row = -1
    for i in range(len(S) - 1, -1, -1):
        if S[i].count("#") == 0:
            delete_row = i
            continue
        break
    if delete_row != -1:
        S = S[:delete_row]

    # 右回転
    S = ["".join(list(x)) for x in zip(*S[::-1], strict=False)]

    # 上部（左部）の白行を削除
    delete_row = -1
    for i in range(len(S)):
        if S[i].count("#") == 0:
            delete_row = i
            continue
        break
    if delete_row != -1:
        S = S[delete_row + 1 :]

    # 下部（右部）の白行を削除
    delete_row = -1
    for i in range(len(S) - 1, -1, -1):
        if S[i].count("#") == 0:
            delete_row = i
            continue
        break
    if delete_row != -1:
        S = S[:delete_row]

    # 左回転
    S = ["".join(list(x)) for x in zip(*S, strict=False)][::-1]

    for s in S:
        print(s)


if __name__ == "__main__":
    main()
