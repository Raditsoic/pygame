import pygame
from pygame.math import Vector2
from sys import exit
import random

class Game():

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.highscore = 0

    def update(self):
        self.snake.move()
        self.check_eat()
        self.check_hit()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()
        self.draw_score()
        self.draw_highscore()

    def draw_score(self):
        score = len(self.snake.body) - 3
        score_surf = font.render(str(score), True, (207, 192, 32))
        score_rect = score_surf.get_rect(center = (cell_size * cell_xy // 2, cell_size * 3))
        screen.blit(score_surf, (score_rect))

        if score > self.highscore:
            self.highscore = score

    def draw_highscore(self):
        highscore = self.highscore
        hs_surf = font.render(str(highscore), True, (136, 118, 234))
        hs_rect = hs_surf.get_rect(center = (cell_size * (cell_xy - 3), cell_size * (cell_xy - 3)))
        screen.blit(hs_surf, (hs_rect))

    def check_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random_position()
            self.snake.add_body()

        for chunk in self.snake.body:
            if chunk == self.fruit.pos:
                self.fruit.random_position()
    
    def check_hit(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= cell_xy * cell_size:
            self.gameover()

        if self.snake.body[0].y < 0 or self.snake.body[0].y >= cell_xy * cell_size:
            self.gameover()

        for chunk in self.snake.body[1:]:
            if self.snake.body[0] == chunk:
                self.gameover()

    def gameover(self):
        self.snake.reset()


class Fruit:

    def __init__(self):
        self.random_position()

    def draw(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, (207, 32, 93), fruit_rect)

    def random_position(self):
        self.x = random.randint(0,cell_xy - 1)
        self.y = random.randint(0, cell_xy - 1 )
        self.pos = Vector2(cell_size * self.x, cell_size * self.y)


class Snake:
    
    def __init__(self):
        self.body = [Vector2(7 * cell_size ,10 * cell_size), Vector2(6 * cell_size, 10 * cell_size), Vector2(5 * cell_size , 10 * cell_size)]
        self.direction = Vector2(1 * cell_size,0)
        self.new_body = False
        

    def draw(self):
        for cell in self.body:
            body_rect = pygame.Rect(cell.x, cell.y, cell_size, cell_size)
            pygame.draw.rect(screen, (32, 111, 207), body_rect)

    def move(self):
        if self.new_body == True:
            body = self.body[:]
            body.insert(0, body[0] + self.direction)
            self.body = body[:]
            self.new_body = False
        else:
            body = self.body[:-1]
            body.insert(0, body[0] + self.direction)
            self.body = body[:]

    def add_body(self):
        self.new_body = True

    def reset(self):
        self.body = [Vector2(7 * cell_size ,10 * cell_size), Vector2(6 * cell_size, 10 * cell_size), Vector2(5 * cell_size , 10 * cell_size)]

pygame.init()
cell_size = 30
cell_xy = 20
screen = pygame.display.set_mode((cell_size * cell_xy,cell_size * cell_xy))
pygame.display.set_caption("Snake by Ruu")
clock = pygame.time.Clock()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

font = pygame.font.Font('pixel/p5hatty.ttf', 50)

main = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == screen_update:
            main.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1 * cell_size:
                    main.snake.direction = Vector2(0, -1 * cell_size)
            elif event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1 * cell_size:
                    main.snake.direction = Vector2(1 * cell_size, 0)
            elif event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1 * cell_size:
                    main.snake.direction = Vector2(0, 1 * cell_size)
            elif event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1 * cell_size:
                    main.snake.direction = Vector2(-1 * cell_size, 0)

    screen.fill((150, 190, 37))
    main.draw()

    pygame.display.update()
    clock.tick(60)