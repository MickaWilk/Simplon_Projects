class Distributeur:
    def __init__(self, stock = 100, argent = 11.50):
        self.stock = stock
        self.argent = argent

    def achat_canette(self, stock, argent, prix = 1.50):
        if self.argent < self.rendre_monnaie(self.argent, self.prix):
            print("Pas assez de monnaie pour effectuer la transaction\n")
        else:
            self.stock -= 1
            print(f"Monnaie rendu : {self.rendre_monnaie(self.argent)}\n Stock restant: {self.stock}\n")

    def rendre_monnaie(self, argent, prix):
        return self.argent - self.prix
