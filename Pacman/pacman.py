import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Pacman settings
pacman_size = 20
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 5

# Define walls (example)
walls = [
    pygame.Rect(100, 100, 40, 200),
    pygame.Rect(200, 200, 200, 40),
    pygame.Rect(400, 100, 40, 200),
    pygame.Rect(100, 300, 400, 40),
    # Add more walls as needed
]

def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), pacman_size)

def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

def check_collision(rect):
    for wall in walls:
        if rect.colliderect(wall):
            return True
    return False

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
        if check_collision(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pacman_x += pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
        if check_collision(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pacman_x -= pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
        if check_collision(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pacman_y += pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
        if check_collision(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pacman_y -= pacman_speed

    # Clear screen
    screen.fill(BLACK)

    # Draw walls
    draw_walls()

    # Draw Pacman
    draw_pacman(pacman_x, pacman_y)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
