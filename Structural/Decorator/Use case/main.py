from sandwich import Sandwich
from sandwich_decorator import SandwichDecorator

sandwich = Sandwich("white", "turkey", "provolone")
print(sandwich.get_sandwich())

ham_sandwich = SandwichDecorator(sandwich, "ham")
print(ham_sandwich.get_sandwich())

cheese_sandwich = SandwichDecorator(sandwich, "cheese")
print(cheese_sandwich.get_sandwich())

ext_sandwich = SandwichDecorator(cheese_sandwich, "ext")
print(ext_sandwich.get_sandwich())
