import pygame
import os
from random import randint, choice


pygame.init()

size_window = (50,600)
size_background = (600,3000)
size_hero = (70,50)
size_bot = (42,48)
size_buff = (50,50)
# 


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
FPS = 60
COUNT_BUFF = 5
BUFFS = ["HP","speed_bullet","speed_shoot","immortal","freezing"]

heart_list = list()     
bot_list = list()      
bullet_list_hero = list()
bullet_list_bot = list()


abs_path = os.path.abspath(__file__ +"/..")

hero_image_list = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "hero.png")), size_hero)

bot_image_list = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "bot.png")), size_bot)


heart_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "heart.png")), [30,30])
skull_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "skull.png")), [30,30])
                       

background_image =  pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "background.png")), size_background)

buff_images = [
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "background.png")), size_background),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_bullet_limit.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_bullet_speed.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_freezing.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "b_immortal.png")), size_buff)
]
