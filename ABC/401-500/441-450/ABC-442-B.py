# ABC-442 B - Music Player
# https://atcoder.jp/contests/abc442/tasks/abc442_b
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    Q = getInt()
    A = getIntRow(Q)

    vol = 0
    play = False
    for a in A:
        if a == 1:
            vol += 1
        elif a == 2:
            if vol > 0:
                vol -= 1
        else:
            play = not play

        print("Yes" if play and vol >= 3 else "No")


if __name__ == "__main__":
    main()
