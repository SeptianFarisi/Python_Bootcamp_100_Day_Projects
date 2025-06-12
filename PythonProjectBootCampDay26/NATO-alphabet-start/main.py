import pandas

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_phonetic.iterrows()}
game = True

while game:
    name = input("Enter a word(Type empty to exit): ").upper()
    if name == "":
        break
    else:
        try:
            list_name = [n for n in name.replace(" ", "")]
            nato_list = [nato_dict[l] for l in name]
        except KeyError:
            print("Sorry, only letters in the alphabet please")
        else:
            print(nato_list)