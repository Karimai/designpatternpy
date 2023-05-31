from big_chair import BigChair
from medium_chair import MediumChair
from small_chair import SmallChair


class ChairFactory:
    @staticmethod
    def get_chair(char_type: str):
        if char_type == "big":
            return BigChair()
        elif char_type == "medium":
            return MediumChair()
        return SmallChair()
