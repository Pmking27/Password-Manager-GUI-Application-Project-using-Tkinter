from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
# import pyperclip
import json
#---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for char in range(randint(8, 10))]
    password_symbols=[choice(symbols) for char in range(randint(2, 4))]
    password_numbers=[choice(numbers) for char in range(randint(2, 4))]

    password_list= password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password_created = "".join(password_list)
    password.insert(0,password_created)
    # pyperclip.copy(password_created)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text=website.get()
    email_text=email.get()
    password_text=password.get()
    new_data={
        website_text:{
            "email":email_text,
            "password":password_text
        }
    }
    
    if len(website_text)==0 or len(password_text)==0:
        messagebox.showinfo(title="Oops! Empty Field",message="Please make sure you haven't left any field empty.")
    else:
        it_ok= messagebox.askokcancel(title=website_text,message=f"These is details you entered :\nEmail :{email_text}\nPassword : {password_text}\nIs it ok to save?")    
        if it_ok:
            try:
                with open("data.json","r") as data_file:
                    data=json.load(data_file)
                   
            except FileNotFoundError:        
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)

            else:
                data.update(new_data)
            finally:    
                website.delete(0,END)
                password.delete(0,END)   

# ---------------------------- Find Password------------------------------- # 

def find_password():
    websites=website.get()
    with open("data.json") as data_file:
        try:
            data=json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
        else:    
            if websites in data:
                email=data[websites]["email"]
                password=data[websites]["password"]
                messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
            else:
                messagebox.showinfo(title="Error",message=f"No details for {websites} exists.")    

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.resizable(0,0)
window.config(padx=50,pady=50)
window.iconbitmap(r"logo_icon.ico")

canvas=Canvas(height=200,width=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


website=Entry(width=32)
website.grid(column=1,row=1)
website.focus()
email=Entry(width=50)
email.grid(column=1,row=2,columnspan=2)
email.insert(END,"demo@gamil.com")
password=Entry(width=32)
password.grid(column=1,row=3)

generate_password=Button(text="Generate Password",command=gen_password)
generate_password.grid(column=2,row=3)
add=Button(text="Add",width=38,command=save)
add.grid(column=1,row=4,columnspan=2)
search_website=Button(text="Search",width=14,command=find_password)
search_website.grid(column=2,row=1)

window.mainloop()