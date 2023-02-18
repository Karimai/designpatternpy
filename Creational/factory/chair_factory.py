from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:
    @staticmethod
    def get_chair(char_type:str):
        if char_type == 'big':
            return BigChair()
        elif char_type == 'medium':
            return MediumChair()
        return SmallChair()

