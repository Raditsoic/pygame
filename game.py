import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
font = pygame.font.Font('pixel/p5hatty.ttf', 50)

sky = pygame.image.load('pixel/sky.png').convert()
land = pygame.image.load('pixel/land.png').convert()

mc = pygame.image.load('pixel/char.png').convert_alpha()
mc_rect = mc.get_rect(midbottom = (350,300))


enemy = pygame.image.load('pixel/pinkg.png').convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (100, 300))

text_game = font.render("Tuyuls", False, 'Black')
game_over = font.render("Game Over", False, 'Black')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(sky, (0,0))
    screen.blit(land, (0,300))
    screen.blit(text_game, (360, 50))
    
    mc_rect.x -= 1
    if mc_rect.x < -60:
        mc_rect.x = 800
    screen.blit(mc, mc_rect)
    screen.blit(enemy, enemy_rect)

    if enemy_rect.colliderect(mc_rect) == 1:
        screen.blit(game_over, (340, 200))
        temp = mc_rect.x
        mc_rect.x = temp


    pygame.display.update()
    clock.tick(60)