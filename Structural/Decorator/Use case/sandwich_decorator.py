from sandwich import Sandwich


class SandwichDecorator:

    def __init__(self, sandwich: Sandwich, ingredient: str):
        self.sandwich = sandwich
        self.ingredient = ingredient

    def get_sandwich(self):
        return self.sandwich.get_sandwich() + ', ' + self.ingredient
