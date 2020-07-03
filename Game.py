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


def select_rock():
    global mylabel
    global user

    mylabel.grid_forget()
    mylabel.destroy()

    mylabel = Label(root, image = image_list[0])
    mylabel.grid(row = 2, column = 0)

    user = "pyimage1"

    Computer_pick()

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black") 
    mylabel2.grid(row = 7, column = 0)

def select_paper():
    global mylabel
    global user

    mylabel.grid_forget()
    mylabel.destroy()

    mylabel = Label(root, image = image_list[1])
    mylabel.grid(row = 2, column = 0)

    user = "pyimage2"

    Computer_pick()

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black")
    mylabel2.grid(row = 7, column = 0)  

def select_scissors():
    global mylabel
    global user

    mylabel.grid_forget()
    mylabel.destroy()

    mylabel = Label(root, image = image_list[2])
    mylabel.grid(row = 2, column = 0)

    user = "pyimage3"

    Computer_pick()

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Black")
    mylabel2.grid(row = 7, column = 0)

def Computer_pick():
    global computer_label
    global computer

    computer_label.grid_forget()
    computer_label.destroy()

    computer = random.choice(image_list)

    computer_label = Label(root, image = computer)
    computer_label.grid(row = 2, column = 2)    

    mylabel3 = Label(root, text = "COMPUTER", fg = "White", bg = "Black")
    mylabel3.grid(row = 7, column = 2)

if user == "pyimage1" and computer == "pyimage2":
        label = Label(root, text = "Computer Won")
        label.grid(row = 8, column = 3)
elif user == "pyimage1" and computer == "pyimage3":
        label2 = Label(root, text = "User Won")
        label.grid(row = 8, column = 1)
elif user == "pyimage2" and computer == "pyimage3":
        label3 = Label(root, text = "Computer Won")
        label.grid(row = 8, column = 1)
elif user == "pyimage2" and computer == "pyimage1":
        label4 = Label(root, text = "User Won")
        label.grid(row = 8, column = 1)
elif user == "pyimage3" and computer == "pyimage1":
        label5 = Label(root, text = "Computer Won")
        label.grid(row = 8, column = 1)
elif user == "pyimage3" and computer == "pyimage2":
        label6 = Label(root, text = "User Won")
        label.grid(row = 8, column = 1)
elif user == "pyimage1" and computer == "pyimage1":
        label7 = Label(root, text = "Draw")
        label.grid(row = 8, column = 1)
elif user == "pyimage2" and computer == "pyimage2":
        label8 = Label(root, text = "Draw")
        label.grid(row = 8, column = 1)
elif user == "pyimage3" and computer == "pyimage1":
        label9 = Label(root, text = "Draw")
        label.grid(row = 8, column = 1)




Rock_Button = Button(root, text = "Rock", command = select_rock)
Rock_Button.grid(row = 0, column = 0)

Paper_Button = Button(root, text = "Paper", command = select_paper)
Paper_Button.grid(row = 0, column = 1)

Scissors_Button = Button(root, text = "Scissors", command = select_scissors)
Scissors_Button.grid(row = 0, column = 2)

root.mainloop()