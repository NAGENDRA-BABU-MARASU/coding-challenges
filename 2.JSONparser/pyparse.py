from JsonParser import JsonException, JsonParser
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Json Parser"
)
parser.add_argument("file_name")
args = parser.parse_args()

file_name = args.file_name
with open(file_name) as f:
    s = f.read()

    try:
        result = JsonParser.parse_json(s)
    except JsonException as e:
        print("The program failed with an error.")
        print(f"[ERROR] - {e}", file=sys.stderr)
        sys.exit(1)

    print(result)
