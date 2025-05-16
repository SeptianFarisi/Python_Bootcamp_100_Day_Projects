from game_data import data
from art import logo, vs
import random

def random_data():
    total = len(data)
    dice = random.randint(1, total - 1)
    list_data = data[dice]
    l = []
    for i in list_data:
        l.append(list_data[i])
    return l

def find_number(data1):
    string_list = data1
    integer_list = 0
    for s in string_list:
        try:
            integer_list += int(s)
        except ValueError:
            pass
    return integer_list

def compare(data1, data2):
    if data1 > data2:
        return True
    else:
        return False

score = 0
compare_a = random_data()
compare_b = random_data()
game = False
print(logo)

while not game:
    if compare_a == compare_b:
        compare_b = random_data()
    number_1 = find_number(compare_a)
    number_2 = find_number(compare_b)

    print(f"Compare A: {compare_a[0]}, {compare_a[1]}, {compare_a[2]}, {compare_a[3]}")
    print(vs)
    print(f"Against B: {compare_b[0]}, {compare_b[1]}, {compare_b[2]}, {compare_b[3]}")
    try:
        answer = input("Who has more followers? Type 'A' or 'B'?").lower()
    except Exception:
        print("Please answer A or B")
    if answer == "a":
        if compare(number_1, number_2) == True:
            score += 1
            print(logo)
            print(f"You're right!. Current score: {score}")
            compare_b = random_data()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game = True
    elif answer == "b":
        if compare(number_2, number_1) == True:
            score += 1
            print(logo)
            print(f"You right. Current score {score}")
            compare_a = compare_b
            compare_b = random_data()
        else:
            print(f"Sorry. Final score {score}")
            game = True