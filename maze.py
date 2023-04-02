from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
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
        if keys_pressed[K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <=650:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 450:
            self.rect.y += self.speed
        if keys_pressed[K_1] and self.speed >= 1:
            self.speed -= 1
        if keys_pressed[K_2] and self.speed <=10:
            self.speed += 1

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       
        self.image = Surface((self.width, self.height))

        self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("fon.jpg"), (win_width, win_height))
#Персонажи игры:
player = Player('hero.png', 10, 440, 1, 50, 50)
monster = Enemy('cyborg.png', 640, 300, 2, 60, 60)
final = GameSprite('treasure.png', 600, 400, 0, 100, 100)
heard = GameSprite('heard2.png', 10, 10, 0, 50, 50)
w1 = Wall(255, 215, 0, 0, 490, 700, 10)
w2 = Wall(255, 215, 0, 0, 0, 700, 10)
w3 = Wall(255, 215, 0, 0, 0, 10, 500)
w4 = Wall(255, 215, 0, 690, 0, 10, 500)
w5 = Wall(255, 215, 0, 450, 100, 10, 600)
w6 = Wall(255, 215, 0, 450, 100, 150, 10)
w7 = Wall(255, 215, 0, 0, 400, 350, 10)
w8 = Wall(255, 215, 0, 340, 100, 10, 300)
speed = 1
game = True
f = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (80, 200, 120))
lose = font.render('YOU LOSE', True, (255, 0, 0))
pr = False
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
    
    if f != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        final.reset()
        heard.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        

        if sprite.collide_rect(player, final):
            print('Победа')
            f = True
            window.blit(win, (200, 200))
        
        while pr != True:
            if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8):
                print('Поражение')
                f = True
                window.blit(lose, (200, 200))
        if sprite.collide_rect(player, monster):
            print('Поражение')
            f = True
            window.blit(lose, (200, 200))
    display.update()
    clock.tick(FPS)
