from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk # python image library
from random import randint
from datetime import time
gui = Tk()
gui.geometry("600x600")
gui.mainloop()
def timer_player():
    global second
    if second > 0:       
        second-=1
        lbl_timer_player = Label(frame_gui, text=("Timer: " +str(second)),fg='#39CCCC',bg='#fff', font=("arial", 15))
        lbl_timer_player.place(x=260,y=540)
        lbl_timer_player.config(bg="#001f3f")
        lbl_timer_player.after(1000,timer_player)

def player_1():
       
        messagebox.showinfo("Time", "Your Time is ended")
        score_user() # note 
        btn_click()
        
def player_2():
    global second, score
    score = 0
    second =0
    print(score)
    print(second)
    Images_list()
def btn_click():
    btn_next = Button(frame_gui, text="Next",fg='#001f3f', font=("arial", 15), command=player_2)
    btn_next.place(x=90,y=400)
def Images_list():
    next_imgs() # calling function to generate new images from list
    #score_user()
    if second == 30:
        timer_player()
    frame_gui.pack(fill="both",expand=1)
    if second == 0:
        player_1()
        
    # create images and global variables to recognize the image
    global user_entry
    global random_1
    global anime_images
    global anime  
    global collectionsOfImage
    # list of images
    collectionsOfImage = ['kirito','yato','tomioka','gojo','zerotwo','natsu','nezuko','akeno']
    """  'ash','ayanokouji','denji','erina','hisoka','kurapika','kuroko','minato',
                        'rias','rimuru','sakuragi','asta','baki','eren','gintoki','gon','hinata',
                        'izumi','shin','takumi','arata','bakugo','haruki','hiro','issei','kaori',
                        'kousei','levi','lilith','mai','mikasa','mitsuha','sakura','yukihira','yuu'
                        ,'garp','anya','law','hancock','kaido','luffy','nami','zoro','robin'] """
    random_1 = randint(0, len(collectionsOfImage)-1) # using random to randomize the images
    anime = "images/" + collectionsOfImage[random_1] + ".png"
    anime_images = ImageTk.PhotoImage(Image.open((anime))) # perfect
    anime_images1 = Label(frame_gui,image= anime_images)
    anime_images1.pack(pady=90)
    # user input
    user_entry = Entry(frame_gui,width=20, font=('Arial',18 ))
    user_entry.place(x = 170,y=445)
    # button next
    btn_next = Button(frame_gui, text="Next",fg='#001f3f', font=("arial", 15), command=Images_list)
    btn_next.place(x=260,y=490)
    # button to check the user input
    btn_ans = Button(frame_gui, text="Submit",fg='#001f3f',font=("arial", 15),command=user_answer)
    btn_ans.place(x=170,y=490)
    # create new form
def next_imgs():
    for widget in frame_gui.winfo_children():
        widget.destroy()
    timer_player()
    frame_gui.pack_forget() 
    # user score
def score_user():
    global score
    lbl_score = Label(frame_gui, text=("Score: "+ str(score)) ,fg='#39CCCC',bg='#fff', font=("arial", 15))
    lbl_score.config(bg="#001f3f")
    lbl_score.place(x=350,y=495)
def scoring():
    global score
    score+=1
    # user answer
def user_answer():
   # calling the function to show the score
    ans = user_entry.get().lower()
    if ans == collectionsOfImage[random_1]:
           messagebox.showinfo("Great", "You got the right answer\n\t" + user_entry.get())
           scoring() # calling the function to increment the score
           Images_list() # everytime the condtion is true the new image will appear
    else:
        messagebox.askretrycancel("Wrong", "Try again")     

frame_gui = Frame(gui, width=400, height=550)
frame_gui.config(bg="#001f3f")
gui.mainloop()