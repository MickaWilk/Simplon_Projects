import streamlit as st
import os
import subprocess

# Énoncé de l'exercice
enonce = """
Exercice : Calcul de la somme

Écrivez une fonction appelée `calculer_somme` qui prend une liste de nombres en entrée et renvoie la somme de tous les éléments dans la liste.
"""

st.title("Exercice Python - Calcul de la somme")
st.write(enonce)

code_input = st.text_area("Copiez votre code Python ici", value="""
def calculer_somme(liste):
\tprint("Hello, World!")
""")


# Bouton pour exécuter les actions
if st.button("Exécuter les tests"):
    # Écrire le code dans le fichier exercice.py
    with open("exercice.py", "w") as file:
        file.write(code_input)
    st.write("Code écrit dans exercice.py")

    # Exécuter les tests avec pytest
    test_result = subprocess.run(["pytest", "test_exercice.py"], stdout=subprocess.PIPE, text=True)
    
    # Stocker le résultat dans results.txt
    with open("results.txt", "w") as file:
        file.write(test_result.stdout)

    st.write("Tests exécutés. Résultats dans results.txt")
