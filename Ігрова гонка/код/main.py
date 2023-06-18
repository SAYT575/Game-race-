from pygame import *
from sys import *
from random import randint
player = "Assets/car1.png"
limit60 = "Assets/60 limit speed.png"
bus1 = "Assets/bus1.png"
car1 = "car1.png"
battery_light = "Assets/Car_Battery_Indicator_Light.png"
check_engine = "Assets/check engine.png"
police_kar = "Assets/police car1.png"
road = "road.png"
transmission = "transmission.png"
car = "car.png"
coin = "coin1.png"
markup = "markup.png"
markup2 = "markup2.png"
win_width = 400
win_height = 800
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class player():
    def __init__(self):
        pass
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.x = randint(-80, 80)
            self.rect.y = 0
class Coin(GameSprite):
    def update(self):
        self.rect.y += self.speed
display.set_caption("Race")
window = display.set_mode((win_width, win_height))
backgroung = transform.scale(image.load(road),(win_width,win_height))
carI = transform.scale(image.load(car1),(100,180))
transmission = transform.scale(image.load(transmission), (40,100))
carLoad = transform.scale(image.load(car),(900,900))
markupLoad = transform.scale(image.load(markup), (100,800))
                                                                            #markup2Load = transform.scale(image.load(markup2), (99,479))
markup_y = -50
markup_x = 160
x1=258
y1=550
speed = 10
run = 1
finish = 0
carsGroup = sprite.Group()
coinGoup = sprite.Group()
for i in range(1,2):                                                        #ЦИКЛ ДЛЯ ДОДАВАННЯ МАШИН
    car = Enemy("car.png", randint(0,300), -409, 120, 190, randint(1,5))
    carsGroup.add(car)
                                                                            #for i in range(1,2):
                                                                            #    coin = Enemy("coin1.png", randint(0,300), - 409, 120, 109, randint(1,5))  #ДОДАВАННЯ МОНЕТ
                                                                            #    carsGroup.add(coin)
x_background = 0
y_background = 0
game_over = False
i=0
a=0
while run:
    window.blit(backgroung,(x_background, y_background))
    window.blit(carI,(x1,y1))
    window.blit(transmission,(340,650))
    carsGroup.update()
    carsGroup.draw(window)
    window.blit(markupLoad,(markup_x,i))
    window.blit(markupLoad,(161,a))
    i+=1                       
    a+=1                                                                
    if i == 800:                     
        i-=800
    if a == 200:
        i-=800
    for e in event.get():
       if e.type == QUIT:
          run = 0
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1 > 17:
        x1 = x1 - speed
    if key_pressed[K_RIGHT] and x1 < 280:
        x1 = x1 + speed
    if key_pressed[K_UP] and y1 > 10:
        y1 = y1 - speed
    if key_pressed[K_DOWN]:
        y1 = y1 + speed
    display.update()




 

    


















    
    
         



 






        



    
    



