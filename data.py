import pygame
import os
from random import randint


pygame.init()

size_window = (3000,600)
size_hero = (60,45)
size_hero = (60,45)
size_bot = (200,200)
# 


BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 144
#15 15
bullet_list_hero = list()
bot_list = list()
bullet_list_bot = list()

abs_path = os.path.abspath(__file__ +"/..")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move2.png")), size_hero)
]
bot1_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move2.png")), size_hero)
]
bot2_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_move2.png")), size_hero)

]
bot3_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_shooter_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_shooter_shoot.png")), size_hero),

]
bullet_image_list =pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "bullet.png")), size_hero)
heart_image_list =pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "health.png")), size_hero)
well_image_list =pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "well.png")), size_hero)
