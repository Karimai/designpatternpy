from composite import Composite
from leaf import Leaf

first_leaf = Leaf("First", 100)
second_leaf = Leaf("Second", 155)

composite = Composite("Capital", 245)

composite.add(first_leaf)
first_leaf.name = "Karim First"
composite.add(second_leaf)
composite.status()
