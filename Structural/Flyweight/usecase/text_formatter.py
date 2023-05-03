"""
The _getitem_ method allows any class to act like a list or dictionary.
"""


class TextFormatter:
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.formatted = []

    class TextRange:
        def __init__(self, start: int, end: int, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position: int):
            return self.start <= position <= self.end

    def get_range(self, start: int, end: int):
        new_range = self.TextRange(start, end)
        self.formatted.append(new_range)
        return new_range

    def __str__(self):
        result = []
        for idx, ch in enumerate(self.plain_text):
            for fmt in self.formatted:
                if fmt.covers(idx) and fmt.capitalize:
                    ch = ch.upper()
            result.append(ch)
        return "".join(result)


if __name__ == "__main__":
    ft = TextFormatter("This is a brave new world!")
    ft.get_range(16, 19).capitalize = True
    print(ft)
