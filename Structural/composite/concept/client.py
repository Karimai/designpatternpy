from leaf import Leaf
from composite import Composite

first_leaf = Leaf('First', 100)
second_leaf = Leaf('Second', 155)

composite = Composite('Capital', 245)

composite.add(first_leaf)
composite.add(second_leaf)
composite.status()

