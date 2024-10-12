import pygame

pygame.init()

WIDTH = 700
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60

# for change font 
# font = pygame.font.Font('')

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run:False

    pygame.display.flip()
pygame.quit()    

            
            