
# coding: utf-8

# # XiamZee by Pygame

# # by Apisit Khomcharoen   6001012630187

# # blog me ---> https://apisit13411.blogspot.com/

# In[1]:


import pygame
import random
from Class_Draw import *                                  # import Class

pygame.init()
pygame.display.set_caption("XiamZee")                     # Set Name display
Display = pygame.display.set_mode((560,620))              # Set display (x,y)
font = pygame.font.SysFont("Bookman Old Style",30)        # Set Font and Size
font2 = pygame.font.SysFont("Bookman Old Style",50)       # Set Font and Size
font3 = pygame.font.SysFont("Bookman Old Style",40)       # Set Font and Size
sound_click = pygame.mixer.music.load("Button-click-sound.mp3")    # Set Sound

# Set Hex color and Set Display color
red = (255,0,0) 
black = (0,0,0)
white = (255,255,255)
blue_button = (68,32,155)
blue_button1 = (68,32,170)
xcolor1 = (139,157,195)
xcolor2 = (59,89,152)
xcolor3= (223,227,238)
Display.fill(white)

# Set Variable
xiamzee = ' '
list_btm_class = []
list_text = []
for i in range (1,28+1):
    list_text.append(str(i))
    
# Set Text color    
def Text_color():                                          
    i=0
    for y in range(200,520,80):              
        for x in range(0,560,80):
            Display.blit(font.render(list_text[i],True,(blue_button)),(x+20,y+20))
            i = i+1
    text3 = font3.render('random xiamzee', True,white)
    Display.blit(text3, (120,550))

# Set GUI  
i = 0
for y in range(200,520,80):              
    for x in range(0,560,80):
        list_btm_class.append(Draw(xcolor1,x,y,80,80))
        Draw(xcolor1,x,y,80,80).Rect()
        Display.blit(font.render(list_text[i],True,(black)),(x+10,y+10))         
        i = i+1   
but_random = Draw(blue_button,0,520,560,100)
but_random.Rect()

# Loop
run = True
while run:
    
    for event in pygame.event.get():                                              # Even in Pygame
        pos = pygame.mouse.get_pos()                                              # Set Position Mouse
        
        # Press Mouse  
        if event.type == pygame.MOUSEBUTTONDOWN:
            Process_btm = pygame.draw.rect(Display,white,(0,100,560,100))         # Set Process
            
            # Codition of MouseButtonDown
           ############### Predict 1st - 28th  ####################
            if list_btm_class[27].Rect().collidepoint(pos):
                xiamzee = '1st : aaa'
            elif list_btm_class[1].Rect().collidepoint(pos):
                xiamzee = '2nd : bbb'
            elif list_btm_class[2].Rect().collidepoint(pos):
                xiamzee = '3rd : ccc'
            elif list_btm_class[3].Rect().collidepoint(pos):
                xiamzee = '4th : ddd'
            elif list_btm_class[4].Rect().collidepoint(pos):
                xiamzee = '5th : eee'
            elif list_btm_class[5].Rect().collidepoint(pos):
                xiamzee = '6th : fff'
            elif list_btm_class[6].Rect().collidepoint(pos):
                xiamzee = '7th : ggg'
            elif list_btm_class[7].Rect().collidepoint(pos):
                xiamzee = '8th : hhh'
            elif list_btm_class[8].Rect().collidepoint(pos):
                xiamzee = '9th : iii'
            elif list_btm_class[9].Rect().collidepoint(pos):
                xiamzee = '10th : jjj'
            elif list_btm_class[10].Rect().collidepoint(pos):
                xiamzee = '11th : kkk'
            elif list_btm_class[11].Rect().collidepoint(pos):
                xiamzee = '12th : lll'
            elif list_btm_class[12].Rect().collidepoint(pos):
                xiamzee = '13th : mmm'
            elif list_btm_class[13].Rect().collidepoint(pos):
                xiamzee = '14th : nnn'
            elif list_btm_class[14].Rect().collidepoint(pos):
                xiamzee = '15th : ooo'
            elif list_btm_class[15].Rect().collidepoint(pos):
                xiamzee = '16th : ppp'
            elif list_btm_class[16].Rect().collidepoint(pos):
                xiamzee = '17th : qqq'
            elif list_btm_class[17].Rect().collidepoint(pos):
                xiamzee = '18th : rrr'
            elif list_btm_class[18].Rect().collidepoint(pos):
                xiamzee = '19th : sss'
            elif list_btm_class[19].Rect().collidepoint(pos):
                xiamzee = '20th : ttt'
            elif list_btm_class[20].Rect().collidepoint(pos):
                xiamzee = '21th : uuu'
            elif list_btm_class[21].Rect().collidepoint(pos):
                xiamzee = '22th : vvv'
            elif list_btm_class[22].Rect().collidepoint(pos):
                xiamzee = '23th : www'
            elif list_btm_class[23].Rect().collidepoint(pos):
                xiamzee = '24th : xxx'
            elif list_btm_class[24].Rect().collidepoint(pos):
                xiamzee = '25th : yyy'
            elif list_btm_class[25].Rect().collidepoint(pos):
                xiamzee = '26th : zzz'
            elif list_btm_class[26].Rect().collidepoint(pos):
                xiamzee = '27th : good luck'
            elif list_btm_class[0].Rect().collidepoint(pos):
                xiamzee = '28th : bad luck'
            text3 = font3.render(xiamzee, True,red)
            Display.blit(text3, (20,100))                                             # Return Text to Display
            
            if but_random.Rect().collidepoint(pos) :                                  # Random Number
                delay_time = 7
                for i in range(30):
                    Process_btm = pygame.draw.rect(Display,white,(0,0,560,100))
                    num_rand = random.randrange(1,28)
                    if i == 29 :
                        text = font2.render('!!! '+str(num_rand)+' !!!', True,red)    # Show your number
                        Display.blit(text, (190,0)) 
                    else : 
                        text = font2.render(str(num_rand), True,red)
                        Display.blit(text, (250,0)) 
                    pygame.time.delay(delay_time)                                   # Set Delay time of random
                    delay_time += 10                                                # add Delay time
                    Text_color()
                    pygame.display.update()                                         # Update Display
            
            pygame.mixer.music.play()                                        # Sound Button
            pygame.mixer.music.play()

       # Change Color when you MouseMotion               
        elif event.type == pygame.MOUSEMOTION:                               
            for i in list_btm_class:
                if i.Rect().collidepoint(pos):               
                    i.set_color(xcolor3)
                else :
                    i.set_color(xcolor1)       
            if but_random.Rect().collidepoint(pos):
                but_random.set_color(blue_button1)
            else :
                but_random.set_color(blue_button)
                 
        elif event.type == pygame.QUIT:                                    
            run= False
            
        Text_color()                                                               # Return Text color
            
    pygame.display.update()                                                        # Update Display
    
pygame.quit()
quit()

