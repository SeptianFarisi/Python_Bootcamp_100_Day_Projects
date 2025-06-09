from tkinter import Tk, Label, Button, Entry

# screen
window = Tk()
window.title("Mile to Kilometers converter project")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

# labels
is_equal_to = Label(text="is equal to", font=("Arial", 12, "normal"))
is_equal_to.grid(column=0, row=1)

number = Label(text="0", font=("Arial", 12, "normal"))
number.grid(column=1, row=1)

mile = Label(text="Miles", font=("Arial", 12, "normal"))
mile.grid(column=2, row=0)
mile.config(padx=10)

km = Label(text="Km", font=("Arial", 12, "normal"))
km.grid(column=2, row=1)

# buttons
def button_clicked():
    temp = float(inputs.get()) * round(1.609344, 2)
    number.config(text=str(temp))
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# entry
inputs = Entry(width=10)
inputs.grid(column=1, row=0)

window.mainloop()