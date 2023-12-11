import argparse
import sys

parser = argparse.ArgumentParser(
    description="cccut - unix cut tool implementation in python"
)
parser.add_argument("-f", type=str, help="give the column number after -f and column numbers start from 0")
parser.add_argument("-d", help="delimiter for generating the output")
parser.add_argument("files", help="give your files separated by a space", type=argparse.FileType('r'), nargs="*")
parser.add_argument('-', help="give this flag to read input from standard input", action='store_const', const='-',
                    dest='stdinput')


class CccutException(Exception):
    pass


def print_column_multi(file, column, delimiter):
    if delimiter is None:
        delimiter = '\t'
    if ',' in column:
        column = column.split(',')
    elif ' ' in column:
        column = column.split(' ')

    column_start = int(column[0])
    column_end = int(column[1])
    print(column_start, column_end)
    # column_length = len(file.readlines()[0].split(delimiter))
    # if column_end >= column_length:
    #     column_end = column_length
    # file.seek(0)
    for line in file.readlines():
        data = line.split(delimiter)
        for column in range(column_start, column_end + 1):
            print(data[column - 1], end=delimiter if column != column_end else '')
        print()


def print_column(file, column, delimiter):
    # delimiter = ',' if file.name[-3:] == 'csv' else '\t'
    if delimiter is None:
        delimiter = '\t'
    if column <= 0:
        raise CccutException("ERROR: fields are numbered with 1")
    # column_length = len(file.readlines()[0].split(delimiter))
    file.seek(0)
    for line in file.readlines():
        # if column <= column_length:
        #     print(line.split(delimiter)[column -1 ])
        # else:
        #     print()
        print(line.split(delimiter)[column - 1])


def main(args):
    try:
        is_stdinput = args.stdinput or not args.files
        file = sys.stdin
        if is_stdinput:
            if ',' in args.f or ' ' in args.f:
                print_column_multi(file, args.f, delimiter=args.d)
            else:
                print_column(file, int(args.f), delimiter=args.d)
        else:
            for file in args.files:
                if ',' in args.f or ' ' in args.f:
                    print_column_multi(file, args.f, delimiter=args.d)
                else:
                    print_column(file, int(args.f), delimiter=args.d)
    except CccutException as e:
        print(e)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
