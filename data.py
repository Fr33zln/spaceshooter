import pygame
import os
from random import randint


pygame.init()

size_window = (995,500)
size_background = (600,3000)
size_hero = (60,45)
size_bot = (60,45)
# 


BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 144
#15 15
well_list = list()
wall_list = list()                
heart_list = list()
bot_list = list()
abs_path = os.path.abspath(__file__ +"/..")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move2.png")), size_hero)
]
bot1_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_stand.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move1.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move2.png")), size_bot)
]

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move2.png")), size_background)





#66 #33 

