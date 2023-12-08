class JsonException(Exception):
    pass


def is_hexadecimal(char_):
    try:
        int(char_, 16)
        return True
    except ValueError:
        return False


class JsonParser:
    def __init__(self):
        self.i = 0
        self.s = ""
        self.depth = 0

    def skip_whitespace(self):
        while self.i < len(self.s) and self.s[self.i] in [" ", "\n", "\t", "\r"]:
            self.i += 1

    def process_string(self):
        try:
            if self.s[self.i] == '"':
                result = ""
                self.i += 1
                self.skip_whitespace()
                while self.s[self.i] != '"':
                    if self.s[self.i] == '\\':
                        char = self.s[self.i + 1]
                        if char in ['"', "\\", "/", "b", "f", "n", "r", "t"]:
                            result += char
                            self.i += 1
                        elif char == 'u':
                            if is_hexadecimal(self.s[self.i + 2]) \
                                    and is_hexadecimal(self.s[self.i + 3]) \
                                    and is_hexadecimal(self.s[self.i + 4]) \
                                    and is_hexadecimal(self.s[self.i + 5]):
                                result += chr(int(self.s[self.i + 2: self.i + 6], 16))
                                self.i += 5
                        else:
                            raise JsonException('Invalid JSON: Illegal backslash escape sequence')
                    else:
                        if self.s[self.i] == '\t':
                            raise JsonException('Invalid Json : tab character in string')

                        elif self.s[self.i] == '\n':
                            raise JsonException('Invalid Json : line break in string')
                        else:
                            result += self.s[self.i]
                    self.i += 1

                self.i += 1
                return result
            # else:
            #     raise JsonException("Invalid Json : Missing starting quote for key")
        except IndexError:
            raise JsonException("Invalid Json : Missing quote at the end")

    def process_colon(self):
        if self.s[self.i] != ':':
            raise JsonException("Invalid Json : expected ':'")
        self.i += 1

    def process_comma(self):
        if self.s[self.i] != ',':
            raise JsonException("Invalid Json : expected ','")
        self.i += 1

    def parse_object(self):
        if self.s[self.i] == "{":
            self.i += 1
            self.depth += 1
            result = {}
            initial = True
            self.skip_whitespace()

            while self.s[self.i] != "}":

                if not initial:
                    self.skip_whitespace()
                    self.process_comma()
                    self.skip_whitespace()

                key = self.process_string()
                self.skip_whitespace()
                self.process_colon()
                self.skip_whitespace()
                value = self.parse_value()
                result[key] = value
                self.skip_whitespace()
                initial = False

            self.i += 1
            self.depth -= 1
            return result

    def parse_number(self):
        start = self.i

        if self.s[self.i] == '-':
            self.i += 1

        if self.s[self.i] == '0':
            self.i += 1
        elif self.s[self.i].isnumeric():
            self.i += 1
            while self.s[self.i].isnumeric():
                self.i += 1

        if self.s[self.i] == '.':
            self.i += 1
            while self.s[self.i].isnumeric():
                self.i += 1

        if self.s[self.i].lower() == 'e':
            self.i += 1
            if self.s[self.i] in ['-', '+']:
                self.i += 1
            while self.s[self.i].isnumeric():
                self.i += 1

        if self.i > start:
            try:
                number = float(self.s[start: self.i])
            except ValueError:
                raise JsonException(f'Invalid JSON : Invalid Number (\'{self.s[start: self.i]}\')')
            if float(number) % 1 == 0:
                return int(number)
            else:
                return float

    def parse_keyword(self, name, value):
        if self.s[self.i: self.i + len(name)] == name:
            self.i += len(name)
            return value
        if name == 'null':
            raise JsonException("Invalid JSON : Missing Value")

    def parse_array(self):
        if self.s[self.i] == '[':
            self.i += 1
            self.depth += 1
            if self.depth > 19:
                raise JsonException("Exceeds maximum depth allowed for this parser")
            self.skip_whitespace()
            result = []
            initial = True

            try:
                while self.s[self.i] != ']':
                    if not initial:
                        self.process_comma()
                        self.skip_whitespace()
                    value = self.parse_value()
                    self.skip_whitespace()
                    result.append(value)
                    initial = False
            except IndexError:
                raise JsonException("Invalid JSON : Missing closing bracket")

            self.i += 1
            self.depth -= 1
            return result

    def parse_value(self):
        result = self.process_string()
        if result is None:
            result = self.parse_number()
        if result is None:
            result = self.parse_object()
        if result is None:
            result = self.parse_array()
        if result is None:
            result = self.parse_keyword("true", True)
        if result is None:
            result = self.parse_keyword("false", False)
        if result is None:
            result = self.parse_keyword("null", None)
        return result

    def parse_json(self, s):
        self.i = 0
        self.s = s
        self.depth = 0
        if s[self.i] not in ["[", "{"]:
            raise JsonException("A json payload should be an object or array")
        output = self.parse_value()
        try:
            self.skip_whitespace()
            print(self.s[self.i])
            char = self.s[self.i]
            raise JsonException(f'Invalid JSON: Extra character "{char}" at the end')
        except IndexError:
            pass
        return output
