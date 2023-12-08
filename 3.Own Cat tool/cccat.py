import argparse
import sys

parser = argparse.ArgumentParser(
    prog="cccat",
    description="cccat, a Unix cat command line tool in python"
)

parser.add_argument('files', type=argparse.FileType('r'), nargs='*',
                    help="when files are given the file objects are stored into files[] list")
parser.add_argument('-', action='store_const', const='-', dest='stdinput',
                    help="when - is given as a flag, the input is read from std input, and the same "
                         "thing goes when no files are given")
parser.add_argument('-n', action="store_true",
                    help="flag to prints the line number before each line including empty lines")
parser.add_argument('-b', action="store_true",
                    help="flag to prints the line number before each line excluding empty lines")
args = parser.parse_args()

is_stdinput = args.stdinput or not args.files

if is_stdinput:
    if args.n:
        n = 1
        for line in sys.stdin.readlines():
            print(f'{n} {line}', end="")
            n += 1
    elif args.b:
        n = 1
        for line in sys.stdin.readlines():
            if line != '\n':
                print(f'{n} {line}', end="")
                n += 1
            else:
                print(line, end="")
    else:
        print(sys.stdin.read())
else:
    if args.n:
        for file in args.files:
            n = 1
            for line in file.readlines():
                print(f'{n} {line}', end="")
                n += 1
    elif args.b:
        for file in args.files:
            n = 1
            for line in file.readlines():
                if line != '\n':
                    print(f'{n} {line}', end="")
                    n += 1
                else:
                    print(line, end="")
    else:
        for file in args.files:
            print(file.read(), end="")
        n = 1
        for line in sys.stdin.readlines():
            if line != '\n':
                print(f'{n} {line}', end="")
                n += 1
            else:
                print(line, end="")

