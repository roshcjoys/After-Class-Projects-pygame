import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Player and Enemies")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

player = pygame.Rect(280, 180, 30, 30)

enemies = []

for i in range(7):
    x = random.randint(0, 570)
    y = random.randint(0, 370)
    enemy = pygame.Rect(x, y, 30, 30)
    enemies.append(enemy)

score = 0

font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 570)
            enemy.y = random.randint(0, 370)

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()