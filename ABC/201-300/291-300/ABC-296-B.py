# ABC-296 B - Chessboard
# https://atcoder.jp/contests/abc296/tasks/abc296_b
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(8)
    s.reverse()

    for y in range(8):
        x = s[y].find('*')
        if x >= 0:
            print('%s%d' % (chr(ord('a') + x), y + 1))


if __name__ == "__main__":
    main()
