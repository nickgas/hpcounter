import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HP Tracker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Fonts
font = pygame.font.Font(None, 36)

# HP values
hp1 = 10
hp2 = 10

def draw_screen():
    screen.fill(WHITE)
    
    # Render HP values
    hp1_text = font.render(f"HP1: {hp1}", True, RED)
    hp2_text = font.render(f"HP2: {hp2}", True, GREEN)
    
    # Draw text
    screen.blit(hp1_text, (WIDTH // 2 - 50, HEIGHT // 3))
    screen.blit(hp2_text, (WIDTH // 2 - 50, 2 * HEIGHT // 3))
    
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hp1 += 1
            elif event.key == pygame.K_DOWN:
                hp1 -= 1
            elif event.key == pygame.K_RIGHT:
                hp2 += 1
            elif event.key == pygame.K_LEFT:
                hp2 -= 1
    
    draw_screen()
    
pygame.quit()
