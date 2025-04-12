from function import *


window = pygame.display.set_mode(size_window)
pygame.display.set_caption("SpaceShooter")

clock = pygame.time.Clock()


hero = Hero(
    10,
    10,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    1,
    2
)


background = Background(size_background[1], background_image,1)


game = True
start_time_bot = 0
end_time_bot = 0







while game:
    events = pygame.event.get()
    background.move()


    #rednder_text_hp = font.render(f"x{hero.hp}", True, WHITE)
    #window.blit(heart_image, (10,10))
    #window.blit(render_text_hp, (45,12))



    #MOVE / BLIT
    hero.move(window)
    
    for bot in bot_list:
        bot.move(window)

    for bullet in bullet_list_hero:
        bullet.move(window)    
    for bullet in bullet_list_bot:
        bullet.move(window)
    
    for buff in Buff.buff_list:
        buff.move(window)
        buff.collide(hero,bot_list)
        if buff.active:
            buff.work_time



        #COLLIDE
    hero.collide_enemy(bot_list)
    hero.collide_enemy(bullet_list_bot)
    index_buff = hero.collide_buff(Buff.buff_list)
    if index_buff != -1:

















    #CREATE BOT
    end_time_bot = pygame.time.get_ticks()
    if end_time_bot - start_time_bot > 2000:
        start_time_bot = end_time_bot
        bot_list.append(Bot(
            randint(0, size_window[0] - size_bot[0]),
            -size_bot[1],
            size_bot[0],
            size_bot[1],
            bot1_image_list,
            2     
        ))








    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.kry == pygame.K_a:
                hero.walk["left"] = True
            if event.kry == pygame.K_d:
                hero.walk["right"] = True
            if event.key == pygame.K_SPACE:
                bullet_list_hero.append(Bullet(hero.centerx - 5,hero.y, 10, 20, WHITE, -5, image=None))
                hero.can_shoot = False


        if event.type == pygame.KEYUP:
            if event.type == pygame.K_a:
                hero.walk["left"] = False
            if event.type == pygame.K_d:
                hero.walk["right"] = False

    clock.tick(FPS)
    pygame.display.flip()
