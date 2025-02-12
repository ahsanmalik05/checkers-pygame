import pygame



pygame.init()


pygame.display.set_mode((400, 500))


pygame.display.set_caption('Connect 4')


running = True

while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
