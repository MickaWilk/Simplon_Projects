game_answers = [ "yes",  "yes", "no", "yes" ]
pauline_answers = [ "yes",  "yes", "no", "no" ]

# EXO 1
{print(f"question {i} - {j} ") for i,j in enumerate(game_answers)}

# EXO 2

[print(f"question {i} - {j} ") for i,j in enumerate(game_answers) if j == "yes"]

# EXO 3

print(game_answers.count("yes"))

# EXO 4
print("Game | Pauline")
[print(f"{game_answers[i]} | {pauline_answers[i]}") for i in range(len(game_answers))]

# EXO 4 ANNEXE
vegetables = ["Carotte", "Poireau", "Courgette"]
colors = ["Orange", "Blanche", "Verte"]

[print(f" Le légume nommé {i} est de couleur {j}") for i, j in zip(vegetables, colors)]

# EXO 5

print("Game | Pauline")
[print(f"{game_answers[i]} | {pauline_answers[i]}") for i in range(len(game_answers)) if game_answers[i] == pauline_answers[i]]


# EXO 6

print (sum(1 for i in range(len(game_answers)) if game_answers[i] == pauline_answers[i]))

#EXO 7

def evaluate_matching_between(game_answers, student_answers):

  return sum(1 for i in range(len(game_answers)) if game_answers[i] == student_answers[i])
  
print(evaluate_matching_between(game_answers, pauline_answers))