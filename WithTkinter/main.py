from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk # python image library
from random import randint
from datetime import time
from player1 import *
gui = Tk()
gui.title("Guessing Game")
gui.geometry("600x600")

lbl1 = Label(gui,text="Guess The Character Name",font=("arial", 20,), pady=7)

lbl1.place(x = 130, y=20)
def hide_text():
    lbl1.destroy()
    lbl_2_player.destroy()
    call_images()
     
def call_images():
    Images_list()
    user_answer()
    next_imgs()
    score_user()
    next_imgs()
lbl_2_player = Button(gui, text="2 Players", font=("arial", 20), command=hide_text)
lbl_2_player.place(x=250,y= 250)

gui.mainloop()