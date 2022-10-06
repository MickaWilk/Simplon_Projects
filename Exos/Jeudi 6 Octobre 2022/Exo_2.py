#EXO 2
liste = ["Vaisselle", "Aspirateur", "Toilettes"]
print("Quelle tâche as-tu accompli :\n" + " ".join(liste) + " ?\n")
reponse = input()
if reponse in liste:
    liste.remove(reponse)
    print("C'est fait ! \n" + str(liste))
else: print("Ce n'était pas une tâche")