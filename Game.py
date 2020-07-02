from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.iconbitmap(r'C:\Users\Hakan\Desktop\Hakan\image\icon.ico')
root.title('ROCK SCISSORS PAPER')

RockPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\ROCK.png')
PaperPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\PAPER.png')
ScissorsPhoto = PhotoImage(file = r'C:\Users\Hakan\Desktop\Rock-Scissors-Paper\Images\SCISSORS.PNG')

my_button = Button(root, image = RockPhoto).grid(row = 0, column = 0)
my_button2 = Button(root, image = PaperPhoto).grid(row = 0, column = 1)
my_button3 = Button(root, image = ScissorsPhoto).grid(row = 0, column = 2)








root.mainloop()