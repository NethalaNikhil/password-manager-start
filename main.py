from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
# import pyperclip
import json

def find_password():
    count = 0
    with open("data.json", "r") as file:
        json_data = json.load(file)
        for key in json_data.keys():
            if website_entry.get() == key:
                count +=1
                value = json_data[website_entry.get()]["password"]
                messagebox.showinfo(title="Details", message=f"Email_id/User_name:{email_entry.get()}\nPassword:{value}")
        if count == 0:
            messagebox.showerror(title="ERROR", message="This website does n't exist in the database")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def delete_items():
    website = website_entry.get()
    new_data = {
        website: {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}
        finally:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, )
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_entry = Entry(width=50)
website_entry.focus()
website = website_entry.get()
email_entry = Entry(width=50)
email_entry.insert(0, "nikhilnethala8@gmail.com")
password_entry = Entry(width=32)

generate_button = Button(text="Generate password", command=generate_password)
add_button = Button(text="Add", width=43, command=delete_items)
search_button = Button(text="search", width=15, command=find_password)

website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)
window.mainloop()
