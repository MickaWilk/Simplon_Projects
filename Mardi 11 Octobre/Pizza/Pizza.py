class Pizza:
    cuisson = "feu de bois"
    def __init__(self, name, ingredient):
        self.name = name
        self.ingredient = ingredient
        pass

    def display_pizza(self):
        print(self.name, self.ingredient)

class Calzone(Pizza):
    def __init__(self, name, ingredient, forme):
        Pizza.__init__(self,name,ingredient)
        self.forme = forme

    def display_pizza(self):
        print(self.name, self.ingredient, self.forme)

pizza = Pizza("cocotte", "chocolatine")
pizza.display_pizza()
calzone = Calzone("cocotte", "chocolatine", "rond")
calzone.display_pizza()
