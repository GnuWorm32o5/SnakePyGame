import sys
import pygame
from pygame.math import Vector2
from pygame.display import set_caption


pygame.init()

neon_green = (0, 255, 70) # Snake
near_black = (10, 10, 10) #Background
red = (255, 50, 50)   # Food

cell_size = 30
number_of_cells = 30

class Food:
    def __init__(self):
        self.position = Vector2(5, 6)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) #Dimenzije ekrana   30x30 je 900x900 ekran

pygame.display.set_caption("Zmijica - Snake") #Naslov

clock = pygame.time.Clock()
`
while True:
    for event in pygame.event.get(): # Game loop logic, searches for an event and works if no event quits
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # So you dont have to press the mousebutton all the time :D
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill(near_black) # Coloring the background
    pygame.display.update()
    clock.tick(60) # To make the game run in 60 fps

