import pygame
from engine.Entity import Entity  # Assuming your Entity class is in engine/entity.py
from engine.Input import InputHandler

class Scene:
    def __init__(self):
        self.cell_size = 20
        self.width = 40  # grid width in cells
        self.height = 30  # grid height in cells
        self.snake = []
        self.direction = pygame.K_RIGHT
        self.next_direction = self.direction
        self.food = None
        self.score = 0
        self.font = None
        self.game_over = False
        self.timer = 0
        self.move_delay = 0.1  # seconds per move
        self.input_handler = InputHandler()

    def start(self):

        self.font = pygame.font.SysFont("Arial", 24)
        # Start snake in middle
        start_x = self.width // 2
        start_y = self.height // 2
        self.snake = [
            Entity(start_x * self.cell_size, start_y * self.cell_size, self.cell_size, self.cell_size, (0, 255, 0)),
            Entity((start_x -1) * self.cell_size, start_y * self.cell_size, self.cell_size, self.cell_size, (0, 200, 0)),
            Entity((start_x -2) * self.cell_size, start_y * self.cell_size, self.cell_size, self.cell_size, (0, 150, 0)),
        ]
        self.direction = pygame.K_RIGHT
        self.next_direction = self.direction
        self.spawn_food()
        self.score = 0
        self.game_over = False
        self.timer = 0

    def spawn_food(self):
        import random
        while True:
            fx = random.randint(0, self.width -1)
            fy = random.randint(0, self.height -1)
            food_rect = pygame.Rect(fx * self.cell_size, fy * self.cell_size, self.cell_size, self.cell_size)
            # Check food not on snake
            if not any(segment.rect.colliderect(food_rect) for segment in self.snake):
                self.food = Entity(food_rect.x, food_rect.y, self.cell_size, self.cell_size, (255, 0, 0))
                break

    def update(self, delta_time):
        if self.game_over:
            return

        self.timer += delta_time
        keys = pygame.key.get_pressed()

        # Change direction with arrow keys (no reverse allowed)
        if keys[pygame.K_UP] and self.direction != pygame.K_DOWN:
            self.next_direction = pygame.K_UP
        elif keys[pygame.K_DOWN] and self.direction != pygame.K_UP:
            self.next_direction = pygame.K_DOWN
        elif keys[pygame.K_LEFT] and self.direction != pygame.K_RIGHT:
            self.next_direction = pygame.K_LEFT
        elif keys[pygame.K_RIGHT] and self.direction != pygame.K_LEFT:
            self.next_direction = pygame.K_RIGHT

        if self.timer >= self.move_delay:
            self.timer = 0
            self.direction = self.next_direction
            self.move_snake()
         

    def move_snake(self):
        # Calculate new head position
        head = self.snake[0]
        x, y = head.x, head.y
        if self.direction == pygame.K_UP:
            y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            x += self.cell_size

        # Check wall collision
        if x < 0 or y < 0 or x >= self.width * self.cell_size or y >= self.height * self.cell_size:
            self.game_over = True
            return

        new_head = Entity(x, y, self.cell_size, self.cell_size, (0, 255, 0))

        # Check self collision
        for segment in self.snake:
            if new_head.rect.colliderect(segment.rect):
                self.game_over = True
                return

        self.snake.insert(0, new_head)

        # Check food collision
        if new_head.rect.colliderect(self.food.rect):
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten

    def draw(self, surface):
        surface.fill((0, 0, 0))

        # Draw food
        if self.food:
            self.food.draw(surface)

        # Draw snake segments
        for segment in self.snake:
            segment.draw(surface)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))

        # Draw game over text
        if self.game_over:
            self.start()   


