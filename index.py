import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True





#scorevalue
score = 0
font = pygame.font.Font("light_stories/font2.ttf",32)
textX = 12
textY = 54


#game over
font1 = pygame.font.Font("light_stories/font2.ttf",120)
overX = 170
overY = 250

#highest score
font2 = pygame.font.Font("light_stories/font2.ttf",32)
hscoreX = 12
hscoreY = 8




# #background
background = pygame.image.load("background.jpg")

# background music
mixer.music.load("background.wav")
mixer.music.play(-1)






#icon
pygame.display.set_caption("space game")
icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

#player define
playerImg = pygame.image.load("player.png")
playerImg2 = pygame.transform.scale(playerImg,(105,105))
playerX = 320
playerY = 480
playerChange = 0


#multiple enemy
emenyImg = []
emenyImg2 = []
enemyX = []
enemyY =  []
enemyChangeX = []
enemyChangeY = []
no_of_enemies = 12


for i in range(no_of_enemies):
    emenyImg.append(pygame.image.load("enemy.png"))
    emenyImg2.append(pygame.transform.scale(emenyImg[i],(110,70)))
    enemyX.append( random.randint(0,690))
    enemyY.append(random.randint(17,180))
    enemyChangeX.append(0.7)
    enemyChangeY.append(30)

#bullet
bulletImg = pygame.image.load("bullet.png")
bulletImg1 = pygame.transform.scale(bulletImg,(40,40))
bulletX = 0
bulletY = 480
bulletChangeX = 0
bulletChangeY = 1.7
bulletState = "ready"

def player(x,y):
    screen.blit(playerImg2,(x,y))


def enemy(x,y,i):
    screen.blit(emenyImg2[i], (x,y))

def bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg1,(x+32, y+10))

def iscollision(bulletX,bulletY,enemyX,enemyY):
    distance = math.sqrt((bulletX - enemyX)**2 + (bulletY - enemyY)**2)
    if distance < 28:
        return True
    else:
        return False
    

# font rendering
def scoreshow(x,y):
    text = font.render("score:-" + str(score),True,(255,255,255))
    screen.blit(text,(x,y))

def gameover(x,y):
    text = font1.render("Game Over",True,(255,255,255))
    screen.blit(text,(x,y))

def highscore(x,y):
    text = font2.render("High score:-" + str(score),True,(255,255,255))
    screen.blit(text,(x,y))


#starting the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -0.6
            if event.key == pygame.K_RIGHT:
                playerChange =  0.6
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    fire_sound = mixer.Sound("laser.wav")
                    fire_sound.play()
                    bulletX =playerX 
                    bullet(bulletX,bulletY)




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0

    screen.fill((0,0,0))

    #background
    screen.blit(background,(0,0))

    #changing the player movement
    playerX += playerChange

    if playerX <= 0:
        playerX  = 0
    elif playerX >= 690:
        playerX = 690


    #moment of enemy

    for i in range(no_of_enemies):
        if enemyY[i] > 400:
            for j in range(no_of_enemies):
                gameover(overX,overY)
                enemyY[j] = 2000
                playerY = 2000
            break







        enemyX[i] += enemyChangeX[i]

        if enemyX[i]<=0:
            enemyChangeX[i] = 0.8
            enemyY[i] += enemyChangeY[i]
        elif enemyX [i]>= 690:
            enemyChangeX[i]= -0.8 
            enemyY[i] += enemyChangeY[i]
        collison = iscollision(bulletX,bulletY,enemyX[i],enemyY[i])
        if collison:
            blast_sound = mixer.Sound("explosion.wav")
            blast_sound.play()
            bulletY = 480
            bulletState = "ready"
            score += 1
            enemyX[i] = random.randint(0,690)
            enemyY[i] =  random.randint(17,180)
        enemy(enemyX[i],enemyY[i],i)
                
       
        

    if bulletY <= 0:
        bulletY = 480  
        bulletState = "ready"
    
    #movemnt of bullet
    if bulletState is "fire":
        bullet(bulletX,bulletY)
        bulletY -= bulletChangeY

    








    
    player(playerX,playerY)
    scoreshow(textX,textY)
    highscore(hscoreX,hscoreY)



    pygame.display.update()
pygame.quit()
