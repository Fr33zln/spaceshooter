from function import *


window = pygame.display.set_mode(size_window)
pygame.display.set_caption("SPACESHOOTER")

clock = pygame.time.Clock()




background = Background(
                        size_background[1],
                        background_image,
                        1
)




hero = Hero(
    size_window[0] // 2 - size_hero[0] // 2,
    size_window[1] - size_hero[1] - 20,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    1,
    2
)

bot1 = Bot(
    100,
    335,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    1,
    "vertical",
    radius = 105,
)


font = pygame.font.Font(None, 40)

game = True
while game:
    events = pygame.event.get()
    window.fill(BLACK)


    hero.collide_enemy([bot1])




    #MOVE/BLIT HERO/BOT
    hero.move(window)
    for bot in bot_list:
        bot.move(window)
        bot.shoot(end_time_bot)


    end_time_bot = pygame.time.get_ticks()
    if end_time_bot - start_time_bot > 2000:
        start_time_bot = end_time_bot
        bot_list.append(Bot(
            randint(0, size_window[0] - size_bot[0]),
            - size_bot[1],
            size_bot[0],
            size_bot[1],
            bot_image_list,
            2

        ))



    #BULLET
    for bullet in bullet_list_hero:
        bullet.move(window)
    for bullet in bullet_list_bot:
        bullet.move(window)

    hero.collide(bot_list)
    hero.collide(bullet_list_bot)

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
