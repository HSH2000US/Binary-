# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame



pygame.init()


screen = pygame.display.set_mode((200, 300))


while True:
    screen.fill((255,0,0))
    pygame.display.flip()
    pygame.display.update()

