import pygame

#initialize the pygame
pygame.init()

#create the screeen
screen = pygame.display.set_mode((900,600))

# Title and icon
pygame.display.set_caption("space Invaders")

icon = pygame.image.load('python-games/pygame/spaceship.png')
pygame.display.set_icon(icon)



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    # RGB- RED,GREEN , BLUE        
    screen.fill((255,0,0)) 
    # display should allways be updated to colors , scores and other run time things
    pygame.display.update()       