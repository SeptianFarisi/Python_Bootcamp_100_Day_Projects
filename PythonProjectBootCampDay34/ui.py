from tkinter import Tk, Canvas, Button, Label, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:

    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.resizable(False,False)

        self.label = Label(text=f"Score: {self.quiz.score}",font=("Arial",10,"bold"),fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)

        self.canvas = Canvas(height=250,width=300)
        self.canvas.create_text(150,125,width=280,text="Quiz text",font=("Arial",20,"italic"),tags="text")
        self.canvas.grid(row=1,columnspan=2,pady=40)

        self.true_img = PhotoImage(file="images/true.png")
        self.t_btn = Button(image=self.true_img,pady=40,highlightthickness=0,command=self.true)
        self.t_btn.grid(row=2,column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.f_btn = Button(image=self.false_img,pady=40,highlightthickness=0,command=self.false)
        self.f_btn.grid(row=2,column=1)

        self.next_questions()

        self.window.mainloop()

    def next_questions(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig("text",text=q_text)
        else:
            self.canvas.itemconfig("text",text="You reach the final quiz",justify="center")
            self.t_btn.config(state="disabled")
            self.f_btn.config(state="disabled")
        if self.is_right(True):
            self.window.after_cancel(self.timer)
            self.canvas.config(bg="white")
        else:
            self.window.after_cancel(self.timer)
            self.canvas.config(bg="white")

    def true(self):
        right = True
        self.is_right(self.quiz.check_answer(right))

    def false(self):
        wrong = False
        self.is_right(self.quiz.check_answer(wrong))

    def is_right(self,is_right):
        if is_right == True:
            self.canvas.config(bg="green")
            self.timer = self.window.after(1000, self.next_questions)
        else:
            self.canvas.config(bg="red")
            self.timer = self.window.after(1000,self.next_questions)