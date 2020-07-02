from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

root.iconbitmap(r'C:\Users\Hakan\Desktop\Hakan\image\icon.ico')
root.title('ROCK SCISSORS PAPER')
root.geometry("600x700")
root.resizable(width = False, height = False)

game_list = [
    "Rock",
    "Paper",
    "Scissors"
]

def select_rock():
    mylabel = Label(root, text = "Rock").grid(row = 1, column = 0)

def select_paper():
    mylabel = Label(root, text = "Paper").grid(row = 1, column = 1)

def select_scissors():
    mylabel = Label(root, text = "Scissors").grid(row = 1, column = 2)

def Computer_pick():
    computer_label = Label(root, text = random.choice(game_list)).grid(row = 3, column = 0)


RockPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\ROCK.png')
PaperPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\PAPER.png')
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.PNG')

Rock_Button = Button(root, image = RockPhoto, command = lambda : select_rock()).grid(row = 0, column = 0)
Paper_Button = Button(root, image = PaperPhoto, command = lambda : select_paper()).grid(row = 0, column = 1)
Scissors_Button = Button(root, image = ScissorsPhoto, command = lambda : select_scissors()).grid(row = 0, column = 2)

Computer_Button = Button(root, text = "Computer's Choice", command = lambda : Computer_pick()).grid(row = 5, column = 1)








root.mainloop()