#EXO 1
questions = [
    "Salut tu vas bien ? :",
    "Tu manges beaucoup ou pas beaucoup ? :",
    "Quel age as-tu ? :"
]

answers = [input(i) for i in questions]

def print_answers(l):
    print("Tes réponses :  " + str(l) )