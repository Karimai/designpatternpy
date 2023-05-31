from big_chair import BigChair
from chair_interface import IChair
from medium_chair import MediumChair
from small_chair import SmallChair


class ChairFactory:
    @staticmethod
    def get_chair(chair_type: str) -> IChair | None:
        if "small" in chair_type.lower():
            return SmallChair()
        if "medium" in chair_type.lower():
            return MediumChair()
        if "big" in chair_type.lower():
            return BigChair()
        return None
