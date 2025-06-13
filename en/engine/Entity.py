import pygame

class Entity:
    def __init__(self, x, y, width, height, color=(255, 255, 255), hp=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hp = hp
        self.vx = 0  # velocity x
        self.vy = 0  # velocity y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.alive = True

    def update(self, delta_time):
        # Move entity by velocity
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time
        self.rect.topleft = (self.x, self.y)

        # Check health
        if self.hp <= 0:
            self.alive = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.alive = False

    def is_alive(self):
        return self.alive
