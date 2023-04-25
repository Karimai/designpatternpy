from builder import Builder


class Director:
    """
    Director class, build a complex representation.
    """

    @staticmethod
    def construct() -> Builder:
        """
        Constructs and returns the final product
        """
        return (
            Builder().build_part_one().build_part_two().build_part_three().get_result()
        )
