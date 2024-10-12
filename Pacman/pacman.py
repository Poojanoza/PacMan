import pygame
from board import boards
pygame.init()

WIDTH = 700
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60
levels = boards

def draw_board():
    num1 = ((HEIGHT - 50)//32)
    num2 = (WIDTH // 30)
    for i in range(len(levels)):
        for j in range(len(levels[i])):
            if levels[i][j] == 1:
                pygame.draw.circle(screen,'white',(j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),4)
            if levels[i][j] == 2:
                pygame.draw.circle(screen,'white',(j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),10)    
            
        

# for change font 
# font = pygame.font.Font('')

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run:False
    pygame.display.flip()
pygame.quit()    

            
            