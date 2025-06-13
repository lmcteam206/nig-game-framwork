import pygame
from engine.SceneManager import SceneManager

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
manager = SceneManager(".")

# Auto-start a scene called 'main_scene.py' in any folder
manager.change_scene("main_scene")

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    manager.update(dt)
    manager.draw(screen)
    pygame.display.flip()

pygame.quit()
