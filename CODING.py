import pygame
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")


BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE=(255,125,100)

pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_size = 20
pacman_speed = 5


ghost_x = random.randint(0, WIDTH)
ghost_y = random.randint(0, HEIGHT)
ghost_size = 20


pellets = []
for _ in range(10):
    pellet_x = random.randint(0, WIDTH)
    pellet_y = random.randint(0, HEIGHT)
    pellets.append([pellet_x, pellet_y])


score = 0
lives = 3
running = True
clock = pygame.time.Clock()


while running:
    screen.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed

    
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size)

    
    pygame.draw.circle(screen, ORANGE, (ghost_x, ghost_y), ghost_size)

   
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, 5)

   
    for pellet in pellets[:]:
        if abs(pacman_x - pellet[0]) < pacman_size and abs(pacman_y - pellet[1]) < pacman_size:
            pellets.remove(pellet)
            score += 10
        if score== 100:
            print ("You Won!!!")
            running=False

   
    if abs(pacman_x - ghost_x) < pacman_size and abs(pacman_y - ghost_y) < pacman_size:
        lives -= 1
        ghost_x, ghost_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  # Reset ghost position
        if lives == 0:
            print("Game Over!")
            running = False

   
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))



   
    pygame.display.flip()
    clock.tick(30)
   

pygame.quit()
