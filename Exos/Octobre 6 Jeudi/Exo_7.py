def print_acronym(s):
    ret = "".join([i[0].upper() for i in s.split()])
    print(f"Your acronym : {ret}")
print_acronym("i love you so much that i can't forget you")