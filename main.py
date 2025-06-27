import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

is_circle_generated = False

def draw_circle(coords: list[int]) -> None:
    pygame.draw.circle(SCREEN, "red", coords, 20, 0)

def draw_screen() -> None:
    SCREEN.fill("purple")

def generate_random_coords() -> list[int]:
    return [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGTH)]

running = True
while running:

    if not is_circle_generated:
        is_circle_generated = True
        coords = generate_random_coords()
        draw_screen()
        draw_circle(coords)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            print(coords)

        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

pygame.quit()