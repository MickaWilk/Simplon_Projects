
def print_dic(d):
    print("Votre agenda\n")
    for k,v in d.items():
        print(f" {k} => {v}")

d = {
    "Date" : 12/12/2022,
    "Description" : "Manger des pommes",
    "status" : "pending"
}

print_dic(d)

d["status"] = input("\n\nChange le status:  ")

print_dic(list(d))