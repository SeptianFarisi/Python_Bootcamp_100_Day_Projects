from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    # Hard level
    pass_letter = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password = pass_letter + pass_symbol + pass_number
    random.shuffle(password)
    final_password = "".join(password)

    password_entry.insert(0,string=final_password)
    pyperclip.copy(text=final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if web_entry.get() == "" or email_user_entry.get() == "" or password_entry.get() == "":
        warning = messagebox.showwarning(title="Empty field", message="Please don't leave any fields empty")
    else:
        message = messagebox.askokcancel(title=web_entry.get(), message=f"these are the details entered: \n"
                                                                        f"Email: {email_user_entry.get()}\n"
                                                                        f"Password: {password_entry.get()}")
        if message:
            with open("data.txt", "a+") as data:
                data.write(f"{web_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n")
                web_entry.delete(0,"end")
                password_entry.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.resizable(False,False)

# canvas
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# labels
website_label = Label(text="Website\t\t:",width=15,anchor="w")
website_label.grid(row=1,column=0)

email_user_label = Label(text="Email/Username\t:",width=15,anchor="w")
email_user_label.grid(row=2,column=0)

password_label = Label(text="Password\t:",width=15,anchor="w")
password_label.grid(row=3,column=0)

# entry
web_entry = Entry(width=53)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

email_user_entry = Entry(width=53)
email_user_entry.grid(row=2,column=1,columnspan=2)
email_user_entry.insert(0, "clownjoker310@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

# buttons
generate_pass_button = Button(text="Generate Password",command=generator)
generate_pass_button.grid(row=3,column=2)

add_button = Button(text="Add", width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()