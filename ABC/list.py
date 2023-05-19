import glob
import os


def main():
    files = glob.glob('./*.py')

    f = open('filelist.md', 'w', encoding='UTF-8')
    for file in files:
        fname = os.path.splitext(os.path.basename(file))[0]
        f.write('[%s](%s.md)\n' % (fname, fname))
    f.close()


if __name__ == "__main__":
    main()
