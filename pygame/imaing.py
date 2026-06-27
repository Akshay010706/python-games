import pygame

#initialize the pygame
pygame.init()

#create the screeen
#900 weight and 600 height
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("space Invaders")

icon = pygame.image.load('python-games/pygame/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('python-games/pygame/space-shipplay.png')
playerX = 370
playerY = 400


def player():
    screen.blit(playerimg,(playerX,playerY))


# Game loop
running = True
while running:
    # RGB- RED,GREEN , BLUE        
    screen.fill((255,0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    
    # display should allways be updated to colors , scores and other run time things
    player()
    pygame.display.update()   