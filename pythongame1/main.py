import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rajat Game')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)
player_img = pygame.image.load('spaceship.png')
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0
playere_img = pygame.image.load('octopus.png')
playereX = random.randint(0, 736)
playereY = random.randint(10, 150)
playereX_change = 0.2
playereY_change = 0
playerb_img = pygame.image.load('bull.png')
playerbX = 0
playerbY = 500
playerbY_change = 0.3
playerbX_change = 0
playerb_state = "ready"
# exp = pygame.image.load('explosion.png')
# expX = playereX
# expY = playereY
# exp_state = "ready"
# expX_change = 0.2
# expY_change = 0
#

def player(x, y):
    screen.blit(player_img, (x, y))


def playere(x, y):
    screen.blit(playere_img, (x, y))


def playerb(x, y):
    global playerb_state
    playerb_state = "fire"
    screen.blit(playerb_img, (x + 20, y + 10))

#def collision(playereX, playereY, playerbX, playerbY):
#    distance = math.sqrt((math.pow(playereX - playerbX,2)) + (math.pow(playereY - playerbY,2)))
  #  if distance < 50:
 #       return True
  #  else:
   #     return False

def collision1(playereX, playereY, playerbX, playerbY):
    distance = math.sqrt((math.pow(playereX - playerbX,2)) + (math.pow(playereY - playerbY,2)))
    if distance < 40:
        return True
    else:
        return False

def collision2(playerX, playereX, playerY, playereY):
    distance = math.sqrt((math.pow(playereX - playerX,2)) + (math.pow(playereY - playerY,2)))
    if distance < 60:
        return True
    else:
        return False

# def explosion(x,y):
#     global exp_state
#     exp_state = "fire"
#     screen.blit(exp , (x, y))

def over():
    exp1 = pygame.image.load('game-over.png')
    screen.blit(exp1 , (130, 45))



running = True
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if playerb_state == "ready":
                    playerbX = playerX
                    playerb(playerbX, playerbY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    playereX += playereX_change
    # expX += expX_change
    if playereX <= 0:
        playereY_change = 40
        playereX_change = 0.2
        playereY += playereY_change
        # expY_change = 40
        # expX_change = 0.2
        # expY += playereY_change


    elif playereX > 736:
        playereY_change = 40
        playereX_change = -0.2
        expY_change = 40
        expX_change = -0.2

        playereY += playereY_change
        # expY += expY_change
    if playerbY <= 0:
        playerbY = 500
        playerb_state = "ready"
    if playerb_state is "fire":
        playerb(playerbX, playerbY)
        playerbY -= playerbY_change


    coll1 = collision1(playereX, playereY, playerbX, playerbY)
    if coll1:
        # explosio

        playerb_state = "ready"
        playerbY = 500
        playereX = random.randint(0, 736)
        playereY = random.randint(10, 150)

    coll2 = collision2(playerX, playereX, playerY, playereY)
    if coll2:
        over()
        playerb_state = "ready"
        playerbY = 0
        playereX = 0
        playereY = 0
        playerX = 0
        playerY = 0

    player(playerX, playerY)
    playere(playereX,playereY)
    # explosion(expX, expY)

    pygame.display.update()
