import pygame
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
TILE_SIZE=1

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE=(255,165,0)
BLUE= (0,0,255)
PURPLE=(128,0,128)
PINK=(255,192,203)
GREEN=(0,255,0)

pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_size = 20
pacman_speed = 5


ghost_x = random.randint(0, WIDTH)
ghost_y = random.randint(0, HEIGHT)
ghost_size = 20
ghost2_x = random.randint(0, WIDTH)
ghost2_y = random.randint(0, HEIGHT)
ghost3_x = random.randint(0, WIDTH)
ghost3_y = random.randint(0, HEIGHT)
ghost4_x = random.randint(0, WIDTH)
ghost4_y = random.randint(0, HEIGHT)
ghost5_x = random.randint(0, WIDTH)
ghost5_y = random.randint(0, HEIGHT)
ghost_speed=5
ghost2_speed=5
ghost3_speed=5
ghost4_speed=5
ghost5_speed=5

pellets = []
for _ in range(10):
    pellet_x = random.randint(0, WIDTH)
    pellet_y = random.randint(0, HEIGHT)
    pellets.append([pellet_x, pellet_y])


score = 0
lives = 3
running = True
clock = pygame.time.Clock()
walls=[
    pygame.Rect(100,100,20,100),
    pygame.Rect(200,100,20,100),
    pygame.Rect(300,100,20,100),
    pygame.Rect(400,100,20,100)
]

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
    pygame.draw.circle(screen, PINK, (ghost2_x, ghost2_y), ghost_size)
    pygame.draw.circle(screen, RED, (ghost3_x, ghost3_y), ghost_size)
    pygame.draw.circle(screen, GREEN, (ghost4_x, ghost4_y), ghost_size)
    pygame.draw.circle(screen, PURPLE, (ghost5_x, ghost5_y), ghost_size)
    for wall in walls:
        pygame.draw.rect(screen,BLUE,wall)
    
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
        ghost_x, ghost_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  
        if lives == 0:
            print("Game Over!")
            running = False
    
    if abs(pacman_x - ghost2_x) < pacman_size and abs(pacman_y - ghost2_y) < pacman_size:
        lives -= 1
        ghost2_x, ghost2_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  
        if lives == 0:
            print("Game Over!")
            running = False
    
    if abs(pacman_x - ghost3_x) < pacman_size and abs(pacman_y - ghost3_y) < pacman_size:
        lives -= 1
        ghost3_x, ghost3_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  
        if lives == 0:
            print("Game Over!")
            running = False   
    
    if abs(pacman_x - ghost4_x) < pacman_size and abs(pacman_y - ghost4_y) < pacman_size:
        lives -= 1
        ghost4_x, ghost4_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  
        if lives == 0:
            print("Game Over!")
            running = False     
    
    if abs(pacman_x - ghost5_x) < pacman_size and abs(pacman_y - ghost5_y) < pacman_size:
        lives -= 1
        ghost5_x, ghost5_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)  
        if lives == 0:
            print("Game Over!")
            running = False
    
    ghost_x+= ghost_speed
    if ghost_x<0 or ghost_x > WIDTH:
        ghost_speed *= -1
    ghost2_x+= ghost2_speed
    if ghost2_x<0 or ghost2_x > WIDTH:
        ghost2_speed *= -1
    ghost3_x+= ghost3_speed
    if ghost3_x<0 or ghost3_x > WIDTH:
        ghost3_speed *= -1
    ghost4_x+= ghost4_speed
    if ghost4_x<0 or ghost4_x > WIDTH:
        ghost4_speed *= -1
    ghost5_x+= ghost5_speed
    if ghost5_x<0 or ghost5_x > WIDTH:
        ghost5_speed *= -1
    ghost_y+= ghost_speed
    if ghost_y<0 or ghost_y > HEIGHT:
        ghost_speed *= -1
    ghost2_y+= ghost2_speed
    if ghost2_y<0 or ghost2_y > HEIGHT:
        ghost2_speed *= -1
    ghost3_y+= ghost3_speed
    if ghost3_y<0 or ghost3_y > HEIGHT:
        ghost3_speed *= -1
    ghost4_y+= ghost4_speed
    if ghost4_y<0 or ghost4_y > HEIGHT:
        ghost4_speed *= -1
    ghost5_y+= ghost5_speed
    if ghost5_y<0 or ghost5_y > HEIGHT:
        ghost5_speed *= -1
    
    pacman_x
    if pacman_x<0 or pacman_x>WIDTH:
        pacman_speed*=-1
    pacman_y
    if pacman_y<0 or pacman_y>HEIGHT:
        pacman_speed*=-1

    
  

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))



   
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

