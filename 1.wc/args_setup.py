import argparse
import sys

def args_setup():
    """Function to set up the arguments for the programme"""

    parser = argparse.ArgumentParser(
        description="ccwc (coding challenge word count), a unix wc implementation which "
                    "can be used to get the word, line, character and byte count"

    )

    parser.add_argument(
        "-c",
        nargs="?",
        type=argparse.FileType('r'),
        const=sys.stdin,
        help="prints the number of bytes in each input file."
    )

    parser.add_argument(
        "-l",
        nargs="?",
        type=argparse.FileType('r'),
        const=sys.stdin,
        help="prints the number of lines in each input file."
    )

    parser.add_argument(
        "-m",
        nargs="?",
        type=argparse.FileType('r'),
        const=sys.stdin,
        help="prints the number of characters in each input file."
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        help="A positional argument which can take a file name or standard input when no flag is given.",
    )

    args = parser.parse_args()
    return args
