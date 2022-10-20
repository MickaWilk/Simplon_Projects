

def print_dic(d):
    print("Votre agenda\n")
    for k,v in d.items():
        print(f" {k} => {v}")


def print_answers(l):
    print("Tes réponses :  " + str(l) )


def print_acronym(s):
    ret = "".join([i[0].upper() for i in s.split()])
    print(f"Your acronym : {ret}")