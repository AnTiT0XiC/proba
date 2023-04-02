#Создай собственный Шутер!
from random import *
from pygame import *
SUU = 0
suuu = 0
n = 6
win_width  =1000
win_height = 650
img_back = 'galaxy.jpg'
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
img_bull = 'bullet.png'
background = transform.scale(image.load(img_back), (win_width, win_height))
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, pw, ph):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (pw, ph))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <=940:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y >=0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <=585:
            self.rect.y += self.speed
        if keys_pressed[K_1] and self.speed >= 1:
            self.speed -= 1
        if keys_pressed[K_2] and self.speed <=30:
            self.speed += 1

    def fire(self):
        bullet = Bullet(img_bull, self.rect.x+23, self.rect.top, 20, 20, 30)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):  
        global SUU
        self.rect.y += self.speed
        if self.rect.y >= 670:
            self.rect.y = -40
            self.rect.x = randint(10, 920)
            self.speed = randint(1, 2)
            self.pw = randint(30, 80)
            self.ph = randint(15, 50)
            SUU += 1
            print(SUU)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y <=-20:
            self.kill
rocket = Player('Ship1.png', 300, 585, 20, 65, 65)
#ufo = Enemy('ufo.png', randint(10, 990), 0, 2, 80, 50)

monsters = sprite.Group()
bullets = sprite.Group()

for i in range(1, n):
    monster = Enemy('ufo.png', randint(10, 920), randint(-50, -40), randint(1, 2), 80, 50)
    monsters.add(monster)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
font.init()
font = font.Font(None, 50)
win = font.render('YOU WIN', True, (80, 200, 120))
lose = font.render('YOU LOSE', True, (255, 0, 0))
game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()

    if finish != True:
        window.blit(background,(0, 0))
        if sprite.spritecollide(rocket, monsters, False):
            finish = True
            window.blit(lose, (450, 300))
        collaydes = sprite.groupcollide(bullets, monsters, False, True)
        for c in collaydes:
            suuu = suuu + 1
            monster = Enemy('ufo.png', randint(10, 920), randint(-50, -40), randint(1, 2), 80, 50)
            monsters.add(monster)
            monster = Enemy('ufo.png', randint(10, 920), randint(-50, -40), randint(1, 2), 80, 50)
            monsters.add(monster)
        chet = font.render('Пропущено: ' + str(SUU), True, (80, 200, 120))
        window.blit(chet, (10, 10))
        chet1 = font.render('Счет: ' + str(suuu), True, (80, 200, 120))
        window.blit(chet1, (10, 50))
        if SUU > 5:
            finish = True
            window.blit(lose, (450, 300))

        if suuu >= 100 :
            finish = True
            window.blit(win, (450, 300))
        rocket.reset()
        rocket.update()

        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        display.update()
        clock.tick(60)