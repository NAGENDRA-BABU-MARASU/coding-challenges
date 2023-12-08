from JsonParser import JsonParser, JsonException

json_parser = JsonParser()
filename = "./tests/step4/invalid.json"
import sys

with open(filename) as f:
    s = f.read()
    try:
        result = json_parser.parse_json(s)
    except JsonException as e:
        print("The program failed with an error")
        print(f'[ERROR] - {e}', file=sys.stderr)
        sys.exit(1)
    except IndexError:
        print("Empty Json")
        sys.exit(1)

    print(result)
