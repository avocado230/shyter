from random import randint
from pygame import *
window= display.set_mode((700,500))
display.set_caption('shyter')
fon= transform.scale(image.load('galaxy.jpg'),(700,500))
clock=time.Clock()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()

lost=0
score=0

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y,player_width,player_high):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(player_width,player_high))
        self.player_speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_LEFT] and self.rect.x> 5:
            self.rect.x-=self.player_speed
        if keys[K_RIGHT] and self.rect.x<630:
            self.rect.x+=self.player_speed
    def fire(self):
        pylka= Bullet('bullet.png', 10, self.rect.centerx,self.rect.top,15,20,)
        pylka1.add(pylka)

class Enemy(GameSprite):
    def __init__(self,player_image,player_speed,player_x,player_y,player_width,player_high):
        super().__init__(player_image,player_speed,player_x,player_y,player_width,player_high)
    def update(self):
        self.rect.y+=self.player_speed
        global lost
        if self.rect.y>=500:
            self.rect.y=0
            self.rect.x=randint(50,450)
            lost+=1

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.player_speed
        if self.rect.y<=0:
            self.kill()
    
pylka1=sprite.Group()


nlos=sprite.Group()
for i in range(5):
    nlo= Enemy('ufo.png',randint(1,3),randint(50,450,),0,90,60)
    nlos.add(nlo)




raketka= Player('rocket.png',5,300,400,70,90)

font.init()
text=font.SysFont('Arial',36)
text2=font.SysFont('Arial',200)
wintext=text2.render('WIN',True,(243,192,11))
losetext=text2.render('LOSE',True,(154,235,179))











finish=False
run=True
while run:
    for i in event.get():
        if i.type==QUIT:
            run=False
        if i.type==KEYDOWN:
            if i.key==K_SPACE:
                raketka.fire()

    if finish!= True:
        window.blit(fon,(0,0))
        raketka.update()
        raketka.reset()
        nlos.update()
        nlos.draw(window)
        pylka1.update()
        pylka1.draw(window)
        lost_text= text.render('пропущенно: '+ str(lost),True,(33,222,111))
        score_text=text.render('счёт: '+ str(score),True,(33,222,111))
        window.blit(lost_text,(5,5))
        window.blit(score_text,(5,50))

        collides=sprite.groupcollide(nlos,pylka1,True,True)
        for i in collides:
            score+=1
            nlo= Enemy('ufo.png',randint(1,3),randint(50,450,),0,90,60)
            nlos.add(nlo)
        if score>=11:
            finish=True
            window.blit(wintext,(150,150 ))
        if sprite.spritecollide(raketka,nlos,False) or lost>=3:
            finish=True
            window.blit(losetext,(150,150 ))
            

    display.update()
    clock.tick(60)