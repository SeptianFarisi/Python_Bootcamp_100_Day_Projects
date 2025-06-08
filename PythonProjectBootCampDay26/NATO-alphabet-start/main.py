import pandas

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in nato_phonetic.iterrows()}
game = True

while game:
    name = input("Enter a word(type 0 to exit): ").upper()
    if name == "0":
        game = False
    else:
        list_name = [n for n in name.replace(" ", "")]
        nato_list = [nato_dict.get(l) for l in list_name]
        print(nato_list)

