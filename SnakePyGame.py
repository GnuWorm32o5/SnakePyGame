import sys
import pygame
from pygame.math import Vector2
import random


pygame.init()

green = (173, 204, 96)
dark_green = (43, 51, 24)

cell_size = 30
number_of_cells = 30


class Food:
    def __init__(self):
        self.position = self.generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        position = Vector2(x, y)
        return position
#Treba joj glavu dodati
class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9), Vector2(3,9)]
        self.direction = Vector2(1, 0)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, dark_green, segment_rect, 2, 11)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

pygame.display.set_caption("Zmijica - Snake")

clock = pygame.time.Clock()

food = Food()
snake = Snake()
food_surface = pygame.image.load("Graphics/food.png")

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

                #Ubaciti space kao pauzu

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_a and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_s and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_d and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_UP and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)


    #Drawing game items
    screen.fill(green)
    food.draw()
    snake.draw()


    pygame.display.update()
    clock.tick(60)

