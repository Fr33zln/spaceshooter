import pygame
import os
from random import randint, choice


pygame.init()

size_window = (995,500)
size_background = (600,3000)
size_hero = (60,45)
size_bot = (60,45)
size_buff = (50,50)
# 


BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 144
#15 15
well_list = list()
wall_list = list()                
bullet_list_hero = list()
bullet_list_bot = list()
bot_list = list()b




BUFFS = ["HP", "speed_bullet", "speed_shoot","immortal","freezing"]
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



heart_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "heart.png")), [30,30])
skull_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "skull.png")), [30,30])
                       


background_image =  pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "background.png")), size_background)

buffs_images = [
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "background.png")), size_background),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_bullet_limit.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_bullet_speed.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_freezing.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_immortal.png")), size_buff)
]
