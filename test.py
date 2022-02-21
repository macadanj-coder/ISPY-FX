import pygame

pygame.init()
width=350;
height=400
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('clicked on image')
basketball = pygame.image.load("basketball1.jpg").convert()

x = 100; # x coordnate of image
y = 100; # y coordinate of image
screen.blit(basketball ,  ( x,y)) # paint to screen
pygame.display.flip() # paint screen one time

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if basketball.get_rect().collidepoint(x, y):
                print('clicked on image')
                rect = basketball.get_rect()
                print(rect)
#loop over, quite pygame
pygame.quit()
