from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import csv



# ---------------------------- Generate Password ------------------------------- # 
def generate_password():
    Password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pss = password_letters+ password_symbols + password_numbers
    shuffle(pss)

    password = (''.join(pss))
    Password.insert(0, password)



# ---------------------------- Save the password ------------------------------- # 
def Add_password():
        if len(website.get()) == 0 or len(Password.get()) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {Id} " f"\nPassword: {Password} \nIs it ok to save?")
        if is_ok:
            with open("password.csv", "a") as f:
                writer = csv.writer(f)
                index = [website.get(),Id.get(), Password.get()]
                writer.writerow(index)
                website.delete(0, END)
                Id.delete(0, END)
                Password.delete(0, END)                                           
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

Website_label = Label(text="Website:")
Website_label.grid(column=0, row=0)
ID_label = Label(text="ID/Email:")
ID_label.grid(column=0, row=1)
Password_label = Label(text="Password:", fg='black')
Password_label.grid(column=0, row=2)

website = Entry(width= 40)
website.grid(column=1, row=0)
Id = Entry()
Id.grid(column=1, row=1)
Password = Entry()
Password.grid(column=1, row=2)

Button_generatePassword = Button(text="Generate Password", command=generate_password)
Button_generatePassword.grid(column=2, row=2)
Button_add = Button(text="Add", command=Add_password)
Button_add.grid(column=1, row=3)

window.mainloop()
