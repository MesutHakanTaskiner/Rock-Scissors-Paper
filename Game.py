from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

root.iconbitmap(r'C:\Users\Hakan\Desktop\Hakan\image\icon.ico')
root.title('ROCK SCISSORS PAPER')
root.geometry("700x700")

#root.resizable(width = False, height = False)

RockPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\ROCK.png')
PaperPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\PAPER.png')
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.png')

image_list = [RockPhoto, PaperPhoto, ScissorsPhoto]

user = ""
computer = ""

mylabel = Label(root, text = "")
computer_label = Label(root, text = "")
label = Label(root, text = "")

def select_rock():
    global mylabel
    global user

    mylabel.grid_forget()
    mylabel.destroy()

    mylabel = Label(root, image = image_list[0])
    mylabel.grid(row = 2, column = 0)

    user = image_list[0]

    Computer_pick()

    if_else(user, computer)

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black") 
    mylabel2.grid(row = 7, column = 0)

def select_paper():
    global mylabel
    global user
 
    mylabel.grid_forget()

    mylabel = Label(root, image = image_list[1])
    mylabel.grid(row = 2, column = 0)

    user = image_list[1]

    Computer_pick()

    if_else(user, computer)

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black")
    mylabel2.grid(row = 7, column = 0)  

def select_scissors():
    global mylabel
    global user

    mylabel.grid_forget()
    
    mylabel = Label(root, image = image_list[2])
    mylabel.grid(row = 2, column = 0)

    user = image_list[2]

    Computer_pick()

    if_else(user, computer)

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black")
    mylabel2.grid(row = 7, column = 0)

def Computer_pick():
    global computer_label
    global computer

    computer_label.grid_forget()
   
    computer = random.choice(image_list)

    computer_label = Label(root, image = computer)
    computer_label.grid(row = 2, column = 2)    

    mylabel3 = Label(root, text = "COMPUTER", fg = "White", bg = "Black")
    mylabel3.grid(row = 7, column = 2)
    

def if_else(user, computer):
        global label
        if user == image_list[0] and computer == image_list[1]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
        elif user == image_list[0] and computer == image_list[2]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
        elif user == image_list[1] and computer == image_list[2]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
        elif user == image_list[1] and computer == image_list[0]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
        elif user == image_list[2] and computer == image_list[0]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
        elif user == image_list[2] and computer == image_list[1]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
        elif user == image_list[0] and computer == image_list[0]:
                label.grid_forget()
                label = Label(root, text = "Draw")
                label.grid(row = 8, column = 1)
        elif user == image_list[1] and computer == image_list[1]:
                label.grid_forget()
                label = Label(root, text = "Draw")
                label.grid(row = 8, column = 1)
        elif user == image_list[2] and computer == image_list[2]:
                label.grid_forget()
                label = Label(root, text = "Draw")
                label.grid(row = 8, column = 1)

Rock_Button = Button(root, text = "Rock", command = select_rock)
Rock_Button.grid(row = 0, column = 0)

Paper_Button = Button(root, text = "Paper", command = select_paper)
Paper_Button.grid(row = 0, column = 1)

Scissors_Button = Button(root, text = "Scissors", command = select_scissors)
Scissors_Button.grid(row = 0, column = 2)

root.mainloop()