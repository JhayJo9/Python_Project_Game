from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk # python image library
from random import randint
gui = Tk()
gui.title("Guessing Game")
gui.geometry("600x600")
score = 0
def user_answer():
    score_user()
    ans = user_entry.get().lower()
    if ans == collectionsOfImage[random_1]:
           messagebox.showinfo("Great", "You got the right answer\n\t" + user_entry.get())
           scoring()
           Images_list()
    else:
        messagebox.askretrycancel("Wrong bitch", "Try again?")
       
def Images_list():
    next_imgs() # calling function to generate new images from list
    score_user()
     
    frame_gui.pack(fill="both",expand=1)
    # create images and global variables to recognize the image
    global user_entry
    global random_1
    global anime_images
    global anime  
    global collectionsOfImage
    collectionsOfImage = ['kirito','yato','tomioka','gojo','zerotwo','natsu','nezuko','akeno',
                        'ash','ayanokouji','denji','erina','hisoka','kurapika','kuroko','minato',
                        'rias','rimuru','sakuragi','asta','baki','eren','gintoki','gon','hinata',
                        'izumi','shin','takumi','arata','bakugo','haruki','hiro','issei','kaori',
                        'kousei','levi','lilith','mai','mikasa','mitsuha','sakura','yukihira','yuu'
                        ,'garp','anya']
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
def next_imgs():
    for widget in frame_gui.winfo_children():
        widget.destroy()
    frame_gui.pack_forget() 
def score_user():
    global score
    lbl_score = Label(frame_gui, text=("Score "+ str(score)) ,fg='#39CCCC',bg='#fff', font=("arial", 15))
    lbl_score.config(bg="#001f3f")
    lbl_score.place(x=330,y=495)
    #score+=1
def scoring():
    global score
    score+=1
# create frame
frame_gui = Frame(gui, width=400, height=550)
frame_gui.config(bg="#001f3f")
Images_list() # calling the function
score_user()
lbl1 = Label(gui,text="Guess The Character Name", bg='#fff', fg='#39CCCC' ,font=("arial", 20,), pady=7)
lbl1.config(bg="#001f3f")
lbl1.place(x = 130, y=20)
gui.mainloop()