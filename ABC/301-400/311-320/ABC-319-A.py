# ABC-319 A - Legendary Players
# https://atcoder.jp/contests/abc319/tasks/abc319_a
#
def getString():
    return input()

def main():
    s = getString()
    d = {
        'tourist': 3858,
        'ksun48': 3679,
        'Benq': 3658,
        'Um_nik': 3648,
        'apiad': 3638,
        'Stonefeang': 3630,
        'ecnerwala': 3613,
        'mnbvmar': 3555,
        'newbiedmy': 3516,
        'semiexp': 3481
    }
    print(d[s])

if __name__ == "__main__":
    main()