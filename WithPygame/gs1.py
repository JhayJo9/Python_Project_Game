import pygame, sys
# size of form
wf = 700
hf = 600
# initialization
pygame.init()
clock = pygame.time.Clock()
screen_window = pygame.display.set_mode((wf,hf))
white = 255, 255, 255, 255
# labels and text box
def text1():    
    text_fontSize = pygame.font.SysFont("Arial", 20)
    textBox1 = pygame.Rect(75,75,100,50)
    Btn_text_1 = text_fontSize.render('Check' , True ,white )
    screen_window.blit(Btn_text_1, (200,200))
# importing image
def img1():   
    img_kirito1 = pygame.image.load('C:\\Users\\penal\\Desktop\\Python_Project_Game\\images\yato1.png').convert()
    img_kirito1_c = pygame.transform.scale(img_kirito1,(200,200))
    screen_window.blit(img_kirito1,(300,300))
# creating buttons
def btn1():
    img_btn_check1 = pygame.image.load('C:\\Users\\penal\\Desktop\\Python_Project_Game\\images\\btn_submit1.png').convert()
    screen_window.blit(img_btn_check1, (300,300))
running = True
while running:
    clock.tick(120)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
           sys.exit()
       
    # draw the image to form
    
    img1()
    text1()
    btn1()
    pygame.display.flip()
pygame.quit  