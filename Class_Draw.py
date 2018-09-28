
# coding: utf-8

# In[1]:


import pygame
Display = pygame.display.set_mode((560,620))

class Draw():                                          # Draw 
    
    def __init__ (self,color,x,y,widht,height):    
        self.color = color
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
    def set_color (self,color):                       # you can change color here
        self.color = color
        return self.Rect()
    
    def Rect (self):                                 # Draw Rect on Display
        return pygame.draw.rect(Display,self.color,(self.x,self.y,self.widht,self.height))

