# ABC-422 B - Looped Rope
# https://atcoder.jp/contests/abc422/tasks/abc422_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    H, W = getIntMap()
    S = getStringRow(H)

    hasError = False
    for y in range(H):
        for x in range(W):
            if S[y][x] == ".":
                continue
            black_cell = 0
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#":
                    black_cell += 1
            if black_cell != 2 and black_cell != 4:
                hasError = True
                break
        if hasError:
            break
    print("Yes" if not hasError else "No")


if __name__ == "__main__":
    main()
