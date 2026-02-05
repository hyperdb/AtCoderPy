# ABC-422 A - Stage Clear
# https://atcoder.jp/contests/abc422/tasks/abc422_a
#
def getString():
    return input()


def main():
    S = getString()

    world, stage = S.split("-")

    print(f"{world}-{int(stage) + 1}" if int(stage) < 8 else f"{int(world) + 1}-1")


if __name__ == "__main__":
    main()
