from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

root.iconbitmap(r'C:\Users\Hakan\Desktop\Hakan\image\icon.ico')
root.title('ROCK SCISSORS PAPER')
root.geometry("535x700")

root.resizable(width = False, height = False)

RockPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\ROCK.png')
PaperPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\PAPER.png')
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.png')

image_list = [RockPhoto, PaperPhoto, ScissorsPhoto]

user = ""
computer = ""
user_score = 0
computer_score = 0

mylabel = Label(root, text = "")
computer_label = Label(root, text = "")
label = Label(root, text = "")
user_score_label = Label(root, text = "")
computer_score_label = Label(root, text = "")

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

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Blue") 
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

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Blue")
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

    mylabel2 = Label(root, text = "PLAYER", fg = "White", bg = "Blue")
    mylabel2.grid(row = 7, column = 0)

def Computer_pick():
    global computer_label
    global computer

    computer_label.grid_forget()
   
    computer = random.choice(image_list)

    computer_label = Label(root, image = computer)
    computer_label.grid(row = 2, column = 2)    

    mylabel3 = Label(root, text = "COMPUTER", fg = "White", bg = "Blue")
    mylabel3.grid(row = 7, column = 2)
    

def if_else(user, computer):
        global label
        global user_score_label
        global user_score
        global computer_score_label
        global computer_score

        if user == image_list[0] and computer == image_list[1]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
                computer_score += 1
        elif user == image_list[0] and computer == image_list[2]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
                user_score += 1
        elif user == image_list[1] and computer == image_list[2]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
                computer_score += 1
        elif user == image_list[1] and computer == image_list[0]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
                user_score += 1
        elif user == image_list[2] and computer == image_list[0]:
                label.grid_forget()
                label = Label(root, text = "Computer Won")
                label.grid(row = 8, column = 2)
                computer_score += 1
        elif user == image_list[2] and computer == image_list[1]:
                label.grid_forget()
                label = Label(root, text = "User Won")
                label.grid(row = 8, column = 0)
                user_score += 1
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

        clear_button =  Button(root, text = "Clear score", command = clear)
        clear_button.grid(row = 10, column = 1)

        exit_button = Button(root, text = "Exit!", command = root.quit, bg = "Black", fg = "White")
        exit_button.grid(row = 13, column = 1)

        user_score_label = Label(root, text = user_score)
        user_score_label.grid(row = 9, column = 0)
        computer_score_label = Label(root, text = computer_score)
        computer_score_label.grid(row = 9, column = 2)

def clear():
        global user_score
        global computer_score

        user_score = 0
        computer_score = 0

        label.grid_forget()

        user_score_label = Label(root, text = user_score)
        user_score_label.grid(row = 9, column = 0)
        computer_score_label = Label(root, text = computer_score)
        computer_score_label.grid(row = 9, column = 2)

Rock_Button = Button(root, text = "Rock", command = select_rock)
Rock_Button.grid(row = 0, column = 0)

Paper_Button = Button(root, text = "Paper", command = select_paper)
Paper_Button.grid(row = 0, column = 1)

Scissors_Button = Button(root, text = "Scissors", command = select_scissors)
Scissors_Button.grid(row = 0, column = 2)


root.mainloop()