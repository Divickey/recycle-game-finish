import pygame
import time
import random

pygame.init()

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("recycle")

def changeBackground(img):
    background = pygame.image.load("bg.png")
    bg = pygame.transform.scale(background,(screen_width, screen_height))
    screen.blit(bg, (0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        #fetch the properties of parent class
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Ritems(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

class NRitems(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()

#list of images for recyclable class
images = ["item1.png", "item2.png", "item3.png"]

#create sprite groups
item_list = pygame.sprite.Group() #recyclable
plastic_list = pygame.sprite.Group() #non-recyclable
allsprites = pygame.sprite.Group()

#Object for bin class
bin = Bin()
allsprites.add(bin)

#create recyclable item sprites
for i in range(50):
    item  = Ritems(random.choice(images))
    item.rect.x=random.randrange(screen_width)
    item.rect.y=random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

#create non recyclable item sprites
for i in range(20):
    plastic = NRitems()
    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

#initialize essential variables
#define colour
WHITE = (255,255,255)
RED = (255,0,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time() #fetch the current time

#font to print score on screen
myFont = pygame.font.SysFont("Comic Sans", 22)
text = myFont.render("score = " +str(0), True, WHITE) #str = string

while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing:False

    timeElapsed=time.time()-start_time
    if timeElapsed >= 60:
        if score >= 20:
            screen.fill("green")
            text = myFont.render("you recycled", True, RED)
        if score  < 20:
            screen.fill("red")
            text = myFont.render("you are a filthy litterer", True, WHITE)
        screen.blit(text,(250,40))
    else:
        changeBackground("bg.png")
        countDown = myFont.render("time left: " +str(60 - int(timeElapsed)), True, WHITE)
        screen.blit(countDown,(20,10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y +=5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 850:
                bin.rect.x += 5
        #recyclable item
        item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)
        for item in item_hit_list:
            score +=1
            text = myFont.render("score = " + str(score), True, WHITE)
        plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)
        for item in plastic_hit_list:
            score -=5
            text = myFont.render("score = " + str(score), True, WHITE)

    screen.blit(text, (20,50))
    allsprites.draw(screen)
    pygame.display.update()
pygame.quit()
