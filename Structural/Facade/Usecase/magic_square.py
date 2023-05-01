from random import randint


class Generator:
    @staticmethod
    def generator(count: int):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    @staticmethod
    def split(array):
        row_count = len(array)
        col_count = len(array)
        result = (
            [r for r in array]
            + [[array[r][c] for r in range(row_count)] for c in range(col_count)]
            + [[array[r][r] for r in range(row_count)]]
            + [[array[r][row_count - r - 1] for r in range(row_count)]]
        )
        return result


class Verifier:
    @staticmethod
    def verify(arrays):
        return all(sum(lst) == sum(arrays[0]) for lst in arrays[1:])


class MagicSquareGenerator:
    @staticmethod
    def generate(size):
        g = Generator()
        s = Splitter()
        v = Verifier()

        while True:
            square = []
            for x in range(size):
                square.append(g.generator(size))
            if v.verify(s.split(square)):
                break
        return square


if __name__ == "__main__":
    gen = MagicSquareGenerator()
    square = gen.generate(4)
    print(square)
    # square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    # square = [[6, 7, 5], [5, 6, 7], [7, 5, 6]]
    # square = [[6, 1, 5], [3, 4, 5], [3, 7, 2]]
