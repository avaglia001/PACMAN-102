import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Pac-Man data
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_size = 20
pacman_speed = 5

# Ghost data
ghost_x = random.randint(0, WIDTH)
ghost_y = random.randint(0, HEIGHT)
ghost_size = 20

# Pellet data
pellets = []
for _ in range(10):
    pellet_x = random.randint(0, WIDTH)
    pellet_y = random.randint(0, HEIGHT)
    pellets.append([pellet_x, pellet_y])

# Game data
score = 0
lives = 3
running = True
clock = pygame.time.Clock()

# Game loop
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement with basic keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size)

    # Draw ghost
    pygame.draw.circle(screen, RED, (ghost_x, ghost_y), ghost_size)

    # Draw pellets
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, 5)

    # Collision with pellets
    for pellet in pellets[:]:
        if abs(pacman_x - pellet[0]) < pacman_size and abs(pacman_y - pellet[1]) < pacman_size:
            pellets.remove(pellet)
            score += 10

    # Collision with ghost
    if abs(pacman_x - ghost_x) < pacman_size and abs(pacman_y - ghost_y) < pacman_size:
        lives -= 1
        ghost_x, ghost_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  # Reset ghost position
        if lives == 0:
            print("Game Over!")
            running = False

    # Display score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
