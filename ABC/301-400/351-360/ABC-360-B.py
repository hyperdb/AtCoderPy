# ABC-360 B - Vertical Reading
# https://atcoder.jp/contests/abc360/tasks/abc360_b
#
def getStringMap():
    return input().split()


def splitStr(s, n):
    i = 0
    j = n
    x, y = divmod(len(s), n)

    result = []

    for _ in range(x):
        result.append(s[i:j])
        i += n
        j += n

    if y > 0:
        result.append(s[(-1 * y) :])

    return result


def rotate(arr, t):
    w = len(arr[0])

    for i in range(w):
        s = ""
        for j in range(len(arr)):
            if len(arr[j]) > i:
                s += arr[j][i]
        if t == s:
            return True

    return False


def main():
    S, T = getStringMap()

    r = False
    for w in range(1, len(S)):
        # w文字に分割
        a = splitStr(S, w)
        # n文字目を結合してTと比較
        if rotate(a, T):
            r = True
            break
    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
