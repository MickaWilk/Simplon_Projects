
def print_answers(l):
    print("Tes réponses :  " + str(l) )


def print_dic(d):
    print("\nQuestions => Reponses\n")
    for k,v in d.items():
        print(f" {k} => {v}")


questions = [
 "Does it have clear eyes?",
 "Is this a male?",
 "Is he vegan?",
 "Is he from Aquitaine?"
]

answers = [input(i) for i in questions]

d_questions = {questions[i] : answers[i] for i in range(len(questions))}

print_answers(answers)
print_dic(d_questions)