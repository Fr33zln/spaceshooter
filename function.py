from data import *





class Plane(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 0
        self.step = step



    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count += 1

class Hero(Plane):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"left":False,"right":False}
        self.hp = hp
        self.start_x = x
        self.start_y = y
        self.time_shoot = 0
        self.can_shoot = True
        self.kill_bot = 0
        self.speed_bullet = -5
        self.shoot_limit = FPS // 5
        self.immortal = False

        

    def move(self, window):
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step

        if True in list(self.walk.values()):
            self.move_image()
        else:
            self.image = self.image_list[0]
        window.blit(self.image, (self.x,self.y))
        self.shoot()

    def shoot(self):
        self.time_shoot += 1
        if self.time_shoot > self.shoot_limit:
            self.can_shoot = True
            self.time_shoot= 0



    def collide_enemy(self, objects):
        index = self.collidelist(objects)
        if index != -1 and not self.immortal:
            self.hp -= 1
            objects.pop(index)

    def collide_buff(self, buff_list):
        return self.collidelist(buff_list)








class Bot(Plane):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)
        self.start_x = x
        self.start_y = y
        self.start_time = 0
        self.random_time = randint(1500, 2700)
        self.freezing = False



    
    def move(self,window):
        self.y += self.step
        window.blit(self.image, (self.x,self.y))



    def shoot(self,time_bot):
        if time_bot - self.start_time > self.random_time:
            self.start_time = time_bot
            self.random_time = randint(1800,2200)
            bullet_list_bot.append(Bullet(self.centerx -5, self.bottom -20, 10, 20,WHITE,4, None))


    def collide(self, objects):
        index = self.collidelist(objects)
        if index != -1:
            if randint(1,100) <= 20:
                create_buff(self.x,self.y)
            bot_list.remove(self)
            objects.pop(index)
            return True
        return False

class Bullet(pygame.Rect):
    def __init__(self,x,y,width,height,color,step,image = None):
        super().__init__(x,y,width,height)
        self.color = color
        self.image = image
        self.start_x = x
        self.start_y = y
        self.step = step


    def move(self, window):
        self.y += self.step
        pygame.draw.rect(window,self.color,self)


    #def collide_hero(self,hero):
        #if self.colliderect(hero):
            #hero.hp =- 1
            #bullet_image_list.remove(self)


class Buff(pygame.Rect):

    buff_list = list()

    def __init__(self,x,y,width,height,image,designed,step,working_time):
        super().__init__(x,y,width,height)
        self.image = image
        self.designed = designed
        self.step = step
        self.time_start = 0
        self.working_time = working_time
        self.active = False

    def move(self,window):
        if not self.active:
            self.y += self.step
            window.blit(self.image, (self.x, self.y))


    def completing(self,hero,bot_list):
        if self.designed == "HP":
            hero.hp += 1
        elif self.designed == "speed_bullet":
            hero.speed_bullet *= 2
            self.time_start = pygame.time.get_ticks()
        elif self.designed == "speed_shoot":
            hero.speed_bullet /= 2
            self.time_start = pygame.time.get_ticks()
        elif self.designed == "immortal":
            hero.immortal = True
            self.time_start = pygame.time.get_ticks()
        elif self.designed == "freezing":
            for bot in bot_list:
                bot.freezing = True
                bot.step = 0
                bot.can_shoot = False
        self.y = size_window[1] +100
        self.step = 0

    def work_time(self,end_time,hero):
        if end_time - self.time._start > self.working_time:
            if self.designed == "speed_bullet":
                hero.speed_bullet /=2
            elif self.designed == "speed_shoot":
                hero.shoot_limit *=2
            elif self.designed == "immortal":
                hero.immortal = False
            print(self)
            Buff.buff_list.remove(self)




    def collide(self,hero, bot_list):
        if self.colliderect(hero) and not self.active:
            self.active = True
            self.completing(hero, bot_list)





def create_buff(x,y):
    index = randint(0,len(BUFFS) -1)
    Buff.buff_list.append(
        Buff(x,y,size_buff[0], size_buff[1], buff_images[index],BUFFS[index], 2, 7000)
        )


class Background():
    def __init__(self,height, image,step):
        self.y1 = 0
        self.y2 = - height
        self.height = height
        self.step = step
        self.image1 = image
        self.image2 = image

    def move(self,window):
        self.y1 += self.step
        self.y2 += self.step

        if self.y1 >= size_window[1]:
            self.y1 = -self.height
        if self.y2 >= size_window[1]:
            self.y2 = -self.height


        window.blit(self.image1, (0, self.y1))
        window.blit(self.image2, (0, self.y2))
