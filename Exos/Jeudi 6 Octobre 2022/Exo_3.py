

def print_dic(d):
    print("Votre agenda\n")
    for k,v in d.items():
        print(f" {k} => {v}")

#EXO 3
d = {
    "31/05/2023" : "Un jour de la semaine",
    "12/12/2029" : "Un jour d'une année",
    "26/10/2024" : "Un évènement spécial",
    "21/01/2025" : "Un rendez vous lointain"
}


print_dic(d)
date=input("Add date of booking (dd/mm/yyyy):  ")
description=input("Add description of booking:  ")
d[date] = description


print_dic(d)