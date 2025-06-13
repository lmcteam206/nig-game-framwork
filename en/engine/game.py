import pygame
from SceneManager import SceneManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Unity-Style Pygame")
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene_manager = SceneManager(game_root_dir=".")
        self.scene_manager.change_scene("IntroScene")  # First scene

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif hasattr(self.scene_manager.current_scene, 'handle_event'):
                    self.scene_manager.current_scene.handle_event(event)

            self.scene_manager.update(delta_time)
            self.screen.fill((30, 30, 30))
            self.scene_manager.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Game().run()
