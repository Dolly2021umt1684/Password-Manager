from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ________________________PASSWORD GENERATOR_______________________#

def Generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[random.choice(letters) for _ in range(0,random.randint(8, 10))]
    password_numbers=[random.choice(numbers) for _ in range(0,random.randint(2, 4))]
    password_symbols=[random.choice(symbols) for _ in range(0,random.randint(2, 4))]

    password_list=password_symbols+password_numbers+password_letters

    random.shuffle(password_list)

    password ="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ________________________SAVE PASSWORD____________________________#

# save password when Add is clicked
def save_password():
    # getting hold of password
    password = password_entry.get()
    # now saving this password
    final_email=email_entry.get()
    website=website_entry.get()
    new_data={
        website:{
            "email": final_email,
            "password":password
        }
    }

    # also keep in mind any of the field should not be empty
    if(len(password)==0 or len(final_email)==0 or len(website)==0):
       messagebox.showinfo(title="alert",message="Please don't leave any field empty")

    else:
        bool_ans=messagebox.askokcancel(title=website,message=f"These are the details entered:\n Email:{final_email}\n Password:{password}\n Is this ok?")
        if bool_ans==True:
            # with open("passwords_entry.txt",mode="a") as new_file:
            #     new_file.write(f"{website} | {final_email} | {password} \n")

            # now we want to keep our data in readable and in a format where we can update it
            # using json
            # with open("password_file.json",mode='w') as file:
            #     # used indent for readability clearity
            #     json.dump(new_data,file,indent=4)
            try:
                with open("password_file.json",'r') as file:
                    # reading data
                    read_data=json.load(file)
                    # print(read_data)
                    # print(type(read_data)
                    # updating the data
                    read_data.update(new_data)


            except FileNotFoundError:
                with open("password_file.json",'w') as file:
                    json.dump(new_data,file,indent=4)

            else:
                with open("password_file.json",'w') as file:
                    json.dump(read_data,file,indent=4)

            finally:
                # now we need to delete the entries which are already filled
                password_entry.delete(0,END)
                website_entry.delete(0,END)
                website_entry.focus()

# ____________________________HANDLING SEARCH BUTTON ________________#


def search_website():
    user_entry = website_entry.get()
    try:

        with open("password_file.json","r") as file:
            data=json.load(file)

    except FileNotFoundError:
           print("there is no prior record")

    else:
            if user_entry in data:
                password = data[user_entry]["password"]
                email = data[user_entry]["email"]
                messagebox.showinfo(title=user_entry, message=f"Email:{email}\n Password:{password}")

            else:
                if user_entry=="":
                  messagebox.showinfo("oops!!", message="please enter the website")

                else:
                  messagebox.showinfo(title="oops!!", message="there exist no password for this website")



# __________________________UI SETUP_______________________________ #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
image_path=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_path) # this returns item id
canvas.grid_configure(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid_configure(row=1,column=0)

email_label=Label(text="email/Username:")
email_label.grid_configure(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid_configure(row=3,column=0)

website_entry=Entry(width=32)
website_entry.grid(row=1,column=1)
website_entry.focus()

search_button=Button(text="Search",width=14,command=search_website)
search_button.grid_configure(row=1,column=2)

email_entry=Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"2021umt1684@mnit.ac.in")

password_entry=Entry(width=32)
password_entry.grid(row=3,column=1)

password_button=Button(text="Generate Password",width=14,command=Generate_password)
password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=43,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()