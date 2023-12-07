import os
import sys
from os import remove
from args_setup import args_setup


def get_byte_count(file_name):
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode('utf-8')
            bytes_size = len(bytes(stdin_content))
            return bytes_size
        else:
            try:
                return os.path.getsize(file_name)
            except FileNotFoundError:
                return f"file {file_name} not found !"
    except OSError:
        return "OS error occurred"


def get_lines_count(file_name):
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode('utf-8')
            line_count = len(stdin_content.splitlines())
            return line_count
        else:
            try:
                file = open(file_name, 'r', encoding='utf-8')
                line_count = len(file.readlines())
                file.close()
                return line_count
            except FileNotFoundError:
                return f"File {file_name} not found !"
    except OSError:
        return "OS error occurred"


def get_word_count(file_name):
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode('utf-8')
            lines = stdin_content.splitlines()
            word_count = 0
            for line in lines:
                word_count += len(line.split())

            return word_count
        else:
            try:
                file = open(file_name, 'r', encoding='utf-8')
                lines = file.readlines()
                word_count = 0
                for line in lines:
                    word_count += len(line.split())
                file.close()
                return word_count
            except FileNotFoundError:
                return f"File {file_name} not found !"
    except OSError:
        return "OS error occurred"


def main(args):
    if args.c:
        if args.c.name != "stdin":
            print(get_byte_count(args.c.name), args.c.name)
        else:
            print(get_byte_count(args.c))
    elif args.l:
        if args.l.name != "stdin":
            print(get_lines_count(args.l.name), args.l.name)
        else:
            print(get_lines_count(args.l))
    elif args.m:
        if args.m.name != "stdin":
            print(get_word_count(args.m.name), args.m.name)
        else:
            print(get_word_count(args.m.name))
    else:
        if args.input_file is not None:
            file_name = args.input_file
            print(get_lines_count(file_name), get_word_count(file_name), get_byte_count(file_name), file_name)
        else:
            stdin_content = sys.stdin.read()
            file_name = "temp.txt"

            file = open(file_name, 'w')
            file.write(stdin_content)

            print(get_lines_count(file_name), get_word_count(file_name), get_byte_count(file_name), file_name)

            remove(file_name)

if __name__ == "__main__":
    args = args_setup()
    main(args)