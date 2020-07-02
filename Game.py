from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

root.iconbitmap(r'C:\Users\Hakan\Desktop\Hakan\image\icon.ico')
root.title('ROCK SCISSORS PAPER')
root.geometry("800x900")
root.resizable(width = False, height = False)

RockPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\ROCK.png')
PaperPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\PAPER.png')
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.png')

image_list = [RockPhoto, PaperPhoto, ScissorsPhoto]

mylabel = Label(root, text = "")
computer_label = Label(root, text = "")

def select_rock():
    global mylabel
    mylabel.grid_forget()
    mylabel.destroy()
    mylabel = Label(root, image = image_list[0])
    mylabel.grid(row = 6, column = 2)

def select_paper():
    global mylabel
    mylabel.grid_forget()
    mylabel.destroy()
    mylabel = Label(root, image = image_list[1])
    mylabel.grid(row = 6, column = 2)

def select_scissors():
    global mylabel
    mylabel.grid_forget()
    mylabel.destroy()
    mylabel = Label(root, image = image_list[2])
    mylabel.grid(row = 6, column = 2)

def Computer_pick():
    global computer_label
    computer_label.grid_forget()
    computer_label.destroy()
    computer_label = Label(root, image = random.choice(image_list))
    computer_label.grid(row = 6, column = 0)

    
    
 

Rock_Button = Button(root, image = RockPhoto, command = select_rock)
Rock_Button.grid(row = 0, column = 0)
Paper_Button = Button(root, image = PaperPhoto, command = select_paper)
Paper_Button.grid(row = 0, column = 1)
Scissors_Button = Button(root, image = ScissorsPhoto, command = select_scissors)
Scissors_Button.grid(row = 0, column = 2)

Computer_Button = Button(root, text = "Computer's Choice", command = Computer_pick).grid(row = 5, column = 1)






root.mainloop()