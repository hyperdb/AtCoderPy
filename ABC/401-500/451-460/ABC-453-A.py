# ABC-453 A - Trimo
# https://atcoder.jp/contests/abc453/tasks/abc453_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()

    # 全部"o"
    if S.count("o") == N:
        print("")
    # 最初の2文字が"o"でない
    elif not (S[0] == "o" and S[1] == "o"):
        print(S)
    # 最初の"o"以外の文字を探して出力
    else:
        for i in range(2, N):
            if S[i] != "o":
                print(S[i:])
                break


if __name__ == "__main__":
    main()
