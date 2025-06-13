import pygame
import sys
import os

class WindowSetup:
    def __init__(self, width=800, height=600, title="Game", fps=60, fullscreen=False, resizable=False):
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center window
        pygame.init()
        self.width = width
        self.height = height
        self.original_size = (width, height)
        self.title = title
        self.fps = fps
        self.fullscreen = fullscreen
        self.resizable = resizable
        self.flags = pygame.RESIZABLE if resizable else 0
        self.clock = pygame.time.Clock()
        self.running = True
        self._init_display()
    
    def _init_display(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()
        else:
            self.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        pygame.display.set_caption(self.title)
    
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        pygame.display.quit()
        pygame.display.init()
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()
        else:
            self.width, self.height = self.original_size
            self.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        pygame.display.set_caption(self.title)
    
    def update(self):
        pygame.display.flip()
        self.clock.tick(self.fps)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.toggle_fullscreen()
    
    def fill(self, color=(0, 0, 0)):
        self.screen.fill(color)
    
    def run(self, render_callback):
        while self.running:
            self.handle_events()
            self.fill()
            render_callback(self.screen)
            self.update()
        pygame.quit()
        sys.exit()
