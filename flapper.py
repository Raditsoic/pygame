import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((735,595))
pygame.display.set_caption("Flapper")
game_text = pygame.font.Font("pixel/p5hatty.ttf", 50)

clock = pygame.time.Clock()
grass = pygame.image.load("pixel/countrys.png")
textstart = game_text.render("Flapper", False, "Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(grass, (0,0))
    screen.blit(textstart, (350, 150))

    pygame.display.update()
    clock.tick(60)