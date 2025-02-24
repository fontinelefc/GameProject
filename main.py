import pygame
print('Start setup')
pygame.init()
window = pygame.display.set_mode(size=(720, 480))
print('Setup End')

print('Loop setup')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() # end pygame

