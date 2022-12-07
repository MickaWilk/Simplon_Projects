import csv, os, pandas as pd

data = pd.read_csv("Students/Files/Aki.csv")
print(data)

d = { "prenoms": ["Thomas","Nariné","Esperance",
          "Mathieu","Louise","Hémon","Quentin",
          "Chouki","Camille","Django","Marie",
          "Matthieu","Laurendi","Lauriane",
          "Rémy","Hugues","Jérôme","Constance",
          "Leona","Hadi","Michaël"],
      "age" : [25,34,32,54,23,56,12,43,15,42,26,42,84,28,27,17,26,18,38,345,46],
      "emojis" : ["\U0001f600", "\U0001F606", "\U0001F923",
                  "\U0001F601", "\U0001F602", "\U0001F603",
                  "\U0001F604", "\U0001F605", "\U0001F607",
                  "\U0001F608", "\U0001F609", "\U0001F610",
                  "\U0001F611", "\U0001F612", "\U0001F613",
                  "\U0001F614", "\U0001F615", "\U0001F616",
                  "\U0001F619", "\U0001F620", "\U0001F621"],
      "arrow" : [[]for i in range(21)]
}
arrow = ["↘️", "➡️","↗️"]


def put_arrows(d):
  count = 0
  for i in d["prenoms"]:
    print(i)
    d["arrow"][count] = "↗️" if len(i) > 7 else "↘️" if len(i) < 7 else "➡️"
    count +=1
  return d

d = put_arrows(d)
df = pd.DataFrame(d)
df.to_csv("Yolo.csv")

print(df)