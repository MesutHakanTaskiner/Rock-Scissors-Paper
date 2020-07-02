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
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.PNG')

image_list = [RockPhoto, PaperPhoto, ScissorsPhoto]
 

def select_rock():
    mylabel = Label(root, image = image_list[0]).grid(row = 6, column = 2)
    mylabel.grid_forget()
    mylabel.delete()

def select_paper():
    mylabel = Label(root, image = image_list[1]).grid(row = 6, column = 2)
    mylabel.grid_forget()
    mylabel.delete()

def select_scissors():
    mylabel = Label(root, image = image_list[2]).grid(row = 6, column = 2)
    mylabel.grid_forget()
    mylabel.delete()

def Computer_pick():
    computer_label = Label(root, image = random.choice(image_list)).grid(row = 6, column = 1)






Rock_Button = Button(root, image = RockPhoto, command = lambda : select_rock()).grid(row = 0, column = 0)
Paper_Button = Button(root, image = PaperPhoto, command = lambda : select_paper()).grid(row = 0, column = 1)
Scissors_Button = Button(root, image = ScissorsPhoto, command = lambda : select_scissors()).grid(row = 0, column = 2)

Computer_Button = Button(root, text = "Computer's Choice", command = lambda : Computer_pick()).grid(row = 5, column = 1)








root.mainloop()