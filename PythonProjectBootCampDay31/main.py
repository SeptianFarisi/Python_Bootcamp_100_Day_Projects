from tkinter import Tk, PhotoImage, Button, Canvas
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
word = {}
learn = {}
try:
    french_word = pd.read_csv("data/data_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    learn = data.to_dict(orient="records")
else:
    learn = french_word.to_dict(orient="records")

def next_card():
    global joker, word
    window.after_cancel(joker)
    word = choice(learn)
    card.itemconfig("img",image=card_front)
    card.itemconfig("title",text="French",fill="black")
    card.itemconfig("word",text=word["French"],fill="black")
    joker = window.after(5000,flip)

def check():
    learn.remove(word)
    print(len(learn))
    data1 = pd.DataFrame(learn)
    data1.to_csv("data/data_to_learn.csv",index=False)
    next_card()

def flip():
    card.itemconfig("img",image=card_back)
    card.itemconfig("title",text="English",fill="white")
    card.itemconfig("word",text=word["English"],fill="white")

# window
window = Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flashy")
window.resizable(False,False)
joker = window.after(5000,flip)

# Canvas
card = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card.create_image(400,263,image=card_front,tags="img")
card.create_text(400,130,text="",font=("Arial",40,"italic"),tags="title")
card.create_text(400,263,text="",font=("Arial",60,"bold"),tags="word")
card.grid(row=0,column=0,columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img,highlightthickness=0,command=check)
right_btn.grid(row=1,column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_btn.grid(row=1,column=0)

next_card()

window.mainloop()