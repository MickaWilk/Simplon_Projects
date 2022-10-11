class Pizza:
    cuisson = "feu de bois"
    def __init__(self, name, ingredient):
        self.name = name
        self.ingredient = ingredient
        pass

    def display_pizza(self):
        print(self.name, self.ingredient)

pizza = Pizza("cocotte", "chocolatine")
pizza.display_pizza()
