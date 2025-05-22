import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        number = self.question_number
        question = self.question_list
        self.question_number += 1
        user_answer = input(f"Q.{number + 1}: {question[number].text} (True or False)? ").title()
        self.check_answer(user_answer, question[number].answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"You current score: {self.score}/{self.question_number}")
        print("\n")